"""
Spanish Learning App - 西语学习积累 📖
"""

import os
import io
import sqlite3
import unicodedata
import urllib.request
import urllib.parse
import json
from datetime import datetime
from flask import Flask, render_template, request, jsonify, send_file

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


@app.route("/psyche-assessment")
def horse_quiz():
    return render_template("horse.html")


@app.route("/virtual-piano")
def virtual_piano():
    return render_template("piano.html")


@app.route("/jimmy-spa")
def jimmy_spa():
    return render_template("spinner.html")


@app.route("/ideas")
def ideas():
    return render_template("ideas.html")


# --- CRUD API ---

@app.route("/api/words", methods=["GET"])
def get_words():
    """获取词汇列表，支持搜索和标签筛选（支持模糊匹配特殊字符如 ñ）"""
    search = request.args.get("search", "").strip()
    tag = request.args.get("tag", "").strip()
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 50))
    offset = (page - 1) * per_page

    conn = get_db()

    # Register a custom function for accent-insensitive search
    def normalize_text(text):
        if text is None:
            return ""
        # Remove diacritics: ñ->n, á->a, etc.
        nfkd = unicodedata.normalize('NFKD', text)
        return ''.join(c for c in nfkd if not unicodedata.combining(c)).lower()

    conn.create_function("normalize", 1, normalize_text)

    query = "SELECT * FROM words WHERE 1=1"
    params = []

    if search:
        # Search both original and normalized versions
        query += " AND (spanish LIKE ? OR chinese LIKE ? OR example LIKE ? OR normalize(spanish) LIKE ? OR normalize(chinese) LIKE ?)"
        like = f"%{search}%"
        normalized_search = f"%{normalize_text(search)}%"
        params.extend([like, like, like, normalized_search, normalized_search])
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
    """查词典：支持西→中英、中→西、英→西"""
    word = request.args.get("word", "").strip()
    if not word:
        return jsonify({"success": False, "error": "请输入要查询的词"})

    # Detect language direction
    # If contains Chinese characters -> Chinese to Spanish
    # If all ASCII -> could be English or Spanish, try both
    has_chinese = any('\u4e00' <= c <= '\u9fff' for c in word)

    if has_chinese:
        # Chinese → Spanish
        es_result = _translate(word, "zh|es")
        en_result = _translate(word, "zh|en")
        return jsonify({
            "success": True,
            "word": word,
            "direction": "zh→es",
            "spanish": es_result if es_result else {"translation": "未找到", "alternatives": []},
            "english": en_result if en_result else {"translation": "Not found", "alternatives": []},
        })
    else:
        # Try Spanish → Chinese/English first
        zh_result = _translate(word, "es|zh")
        en_result = _translate(word, "es|en")

        # If the translation looks like it just echoed back the same word,
        # it's probably English input, try English → Spanish
        zh_text = zh_result["translation"] if zh_result else ""
        en_text = en_result["translation"] if en_result else ""

        if en_text.lower().strip() == word.lower().strip() or zh_text.lower().strip() == word.lower().strip():
            # Likely English input
            es_result = _translate(word, "en|es")
            zh_from_en = _translate(word, "en|zh")
            return jsonify({
                "success": True,
                "word": word,
                "direction": "en→es",
                "spanish": es_result if es_result else {"translation": "No encontrado", "alternatives": []},
                "chinese": zh_from_en if zh_from_en else {"translation": "未找到", "alternatives": []},
            })

        # Normal Spanish → Chinese/English
        return jsonify({
            "success": True,
            "word": word,
            "direction": "es→zh/en",
            "chinese": zh_result if zh_result else {"translation": "未找到", "alternatives": []},
            "english": en_result if en_result else {"translation": "Not found", "alternatives": []},
        })


# --- Verb Conjugation ---

@app.route("/api/conjugate", methods=["GET"])
def conjugate_verb():
    """查询动词变位"""
    from conjugations import get_conjugation, PRONOUNS, TENSE_NAMES, IRREGULAR_VERBS
    verb = request.args.get("verb", "").strip().lower()
    if not verb:
        return jsonify({"success": False, "error": "请输入动词原形"})

    result = get_conjugation(verb)
    if not result:
        return jsonify({"success": False, "error": f"未找到动词 '{verb}' 的变位。请输入动词原形（如 hablar, comer, vivir）"})

    return jsonify({
        "success": True,
        "verb": verb,
        "meaning": result.get("meaning", ""),
        "meaning_zh": result.get("meaning_zh", ""),
        "is_irregular": verb in IRREGULAR_VERBS,
        "pronouns": PRONOUNS,
        "tense_names": TENSE_NAMES,
        "conjugations": {k: v for k, v in result.items() if k not in ("meaning", "meaning_zh")},
    })


@app.route("/api/conjugate/list", methods=["GET"])
def list_verbs():
    """列出所有可查询的不规则动词"""
    from conjugations import IRREGULAR_VERBS
    verbs = [{"verb": v, "meaning": data["meaning"], "meaning_zh": data["meaning_zh"]}
             for v, data in IRREGULAR_VERBS.items()]
    return jsonify({"success": True, "verbs": verbs})


# --- Daily Reading ---

@app.route("/api/reading/today", methods=["GET"])
def today_reading():
    """获取今日阅读"""
    from daily_readings import get_reading_for_today
    reading = get_reading_for_today()
    return jsonify({"success": True, "reading": reading})


@app.route("/api/reading/<int:index>", methods=["GET"])
def get_reading(index):
    """获取指定阅读（支持环形浏览）"""
    from daily_readings import get_reading_by_index, READINGS
    # Wrap around
    index = index % len(READINGS)
    reading = get_reading_by_index(index)
    if not reading:
        return jsonify({"success": False, "error": "未找到该阅读"})
    return jsonify({"success": True, "reading": reading})


# --- Text-to-Speech ---

@app.route("/api/tts", methods=["GET"])
def text_to_speech():
    """生成西语发音音频"""
    text = request.args.get("text", "").strip()
    if not text:
        return jsonify({"success": False, "error": "缺少文本"}), 400

    # Limit text length for safety
    if len(text) > 500:
        text = text[:500]

    try:
        from gtts import gTTS
        tts = gTTS(text=text, lang='es', slow=False)
        audio_buffer = io.BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)
        return send_file(audio_buffer, mimetype='audio/mpeg', download_name='speech.mp3')
    except ImportError:
        return jsonify({"success": False, "error": "gTTS 未安装，请在服务器运行: pip install gtts"}), 500
    except Exception as e:
        return jsonify({"success": False, "error": f"TTS 错误: {str(e)}"}), 500


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
