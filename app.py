"""
Spanish Learning App - 西语学习积累 📖
"""

import os
import sqlite3
import urllib.request
import urllib.parse
import json
from datetime import datetime
from flask import Flask, render_template, request, jsonify

BASE_DIR = os.path.dirname(__file__)
app = Flask(__name__, template_folder=os.path.join(BASE_DIR, "templates"))

# Use /data for persistent storage on Render, local dir otherwise
DATA_DIR = "/data" if os.path.isdir("/data") else BASE_DIR
DB_PATH = os.path.join(DATA_DIR, "spanish.db")


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    return conn


def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS words (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            spanish TEXT NOT NULL,
            chinese TEXT NOT NULL,
            example TEXT DEFAULT '',
            tag TEXT DEFAULT '',
            review_count INTEGER DEFAULT 0,
            last_reviewed TEXT,
            created_at TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


@app.route("/")
def index():
    return render_template("index.html")


# --- CRUD API ---

@app.route("/api/words", methods=["GET"])
def get_words():
    """获取词汇列表，支持搜索和标签筛选"""
    search = request.args.get("search", "").strip()
    tag = request.args.get("tag", "").strip()
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 50))
    offset = (page - 1) * per_page

    conn = get_db()
    query = "SELECT * FROM words WHERE 1=1"
    params = []

    if search:
        query += " AND (spanish LIKE ? OR chinese LIKE ? OR example LIKE ?)"
        like = f"%{search}%"
        params.extend([like, like, like])
    if tag:
        query += " AND tag = ?"
        params.append(tag)

    # Total count
    count_query = query.replace("SELECT *", "SELECT COUNT(*)")
    total = conn.execute(count_query, params).fetchone()[0]

    query += " ORDER BY created_at DESC LIMIT ? OFFSET ?"
    params.extend([per_page, offset])

    words = conn.execute(query, params).fetchall()
    conn.close()

    return jsonify({
        "success": True,
        "words": [dict(w) for w in words],
        "total": total,
        "page": page,
        "per_page": per_page
    })


@app.route("/api/words", methods=["POST"])
def add_word():
    """添加新词汇"""
    data = request.json
    spanish = data.get("spanish", "").strip()
    chinese = data.get("chinese", "").strip()
    example = data.get("example", "").strip()
    tag = data.get("tag", "").strip()

    if not spanish or not chinese:
        return jsonify({"success": False, "error": "西语和中文释义不能为空"})

    conn = get_db()
    conn.execute(
        "INSERT INTO words (spanish, chinese, example, tag, created_at) VALUES (?, ?, ?, ?, ?)",
        (spanish, chinese, example, tag, datetime.now().isoformat())
    )
    conn.commit()
    conn.close()
    return jsonify({"success": True, "message": "添加成功 ✓"})


@app.route("/api/words/<int:word_id>", methods=["PUT"])
def update_word(word_id):
    """更新词汇"""
    data = request.json
    spanish = data.get("spanish", "").strip()
    chinese = data.get("chinese", "").strip()
    example = data.get("example", "").strip()
    tag = data.get("tag", "").strip()

    if not spanish or not chinese:
        return jsonify({"success": False, "error": "西语和中文释义不能为空"})

    conn = get_db()
    conn.execute(
        "UPDATE words SET spanish=?, chinese=?, example=?, tag=? WHERE id=?",
        (spanish, chinese, example, tag, word_id)
    )
    conn.commit()
    conn.close()
    return jsonify({"success": True})


@app.route("/api/words/<int:word_id>", methods=["DELETE"])
def delete_word(word_id):
    """删除词汇"""
    conn = get_db()
    conn.execute("DELETE FROM words WHERE id = ?", (word_id,))
    conn.commit()
    conn.close()
    return jsonify({"success": True})


# --- Review Mode ---

@app.route("/api/review/random", methods=["GET"])
def review_random():
    """随机抽取词汇复习（优先抽复习次数少的）"""
    count = int(request.args.get("count", 10))
    tag = request.args.get("tag", "").strip()

    conn = get_db()
    query = "SELECT * FROM words"
    params = []

    if tag:
        query += " WHERE tag = ?"
        params.append(tag)

    query += " ORDER BY review_count ASC, RANDOM() LIMIT ?"
    params.append(count)

    words = conn.execute(query, params).fetchall()
    conn.close()
    return jsonify({"success": True, "words": [dict(w) for w in words]})


@app.route("/api/review/mark", methods=["POST"])
def mark_reviewed():
    """标记已复习"""
    data = request.json
    word_id = data.get("word_id")

    if not word_id:
        return jsonify({"success": False, "error": "缺少 word_id"})

    conn = get_db()
    conn.execute(
        "UPDATE words SET review_count = review_count + 1, last_reviewed = ? WHERE id = ?",
        (datetime.now().isoformat(), word_id)
    )
    conn.commit()
    conn.close()
    return jsonify({"success": True})


# --- Tags ---

@app.route("/api/tags", methods=["GET"])
def get_tags():
    """获取所有标签"""
    conn = get_db()
    tags = conn.execute(
        "SELECT tag, COUNT(*) as count FROM words WHERE tag != '' GROUP BY tag ORDER BY count DESC"
    ).fetchall()
    conn.close()
    return jsonify({"success": True, "tags": [dict(t) for t in tags]})


# --- Dictionary Lookup ---

def _translate(word, lang_pair):
    """Call MyMemory API for translation"""
    try:
        encoded = urllib.parse.quote(word)
        url = f"https://api.mymemory.translated.net/get?q={encoded}&langpair={lang_pair}"
        req = urllib.request.Request(url, headers={"User-Agent": "SpanishLearningApp/1.0"})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            if data.get("responseStatus") == 200:
                main_translation = data["responseData"]["translatedText"]
                # Get alternative translations from matches
                alternatives = []
                for match in data.get("matches", []):
                    t = match.get("translation", "")
                    if t and t != main_translation and t not in alternatives:
                        alternatives.append(t)
                    if len(alternatives) >= 3:
                        break
                return {"translation": main_translation, "alternatives": alternatives}
    except Exception:
        pass
    return None


@app.route("/api/dictionary/lookup", methods=["GET"])
def dictionary_lookup():
    """查词典：西语 → 中文 + 英文"""
    word = request.args.get("word", "").strip()
    if not word:
        return jsonify({"success": False, "error": "请输入要查询的词"})

    # Spanish → Chinese
    zh_result = _translate(word, "es|zh")
    # Spanish → English
    en_result = _translate(word, "es|en")

    return jsonify({
        "success": True,
        "word": word,
        "chinese": zh_result if zh_result else {"translation": "未找到", "alternatives": []},
        "english": en_result if en_result else {"translation": "Not found", "alternatives": []},
    })


# --- Stats ---

@app.route("/api/stats", methods=["GET"])
def get_stats():
    """获取学习统计"""
    conn = get_db()
    total = conn.execute("SELECT COUNT(*) FROM words").fetchone()[0]
    reviewed = conn.execute("SELECT COUNT(*) FROM words WHERE review_count > 0").fetchone()[0]
    today_added = conn.execute(
        "SELECT COUNT(*) FROM words WHERE date(created_at) = date('now')"
    ).fetchone()[0]
    conn.close()
    return jsonify({
        "success": True,
        "total": total,
        "reviewed": reviewed,
        "today_added": today_added
    })


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)
