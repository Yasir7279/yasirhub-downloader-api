from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({
        "status": "success",
        "message": "YasirHub Downloader API is running"
    })

@app.route("/api/check", methods=["POST"])
def check_link():
    data = request.get_json(silent=True) or {}
    url = data.get("url", "").strip()

    if not url:
        return jsonify({
            "success": False,
            "message": "Please enter a video URL."
        }), 400

    if "tiktok.com" in url:
        platform = "TikTok"
    elif "instagram.com" in url:
        platform = "Instagram"
    else:
        return jsonify({
            "success": False,
            "message": "Currently only TikTok and Instagram links are supported."
        }), 400

    return jsonify({
        "success": True,
        "platform": platform,
        "url": url,
        "message": f"{platform} link detected successfully."
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
