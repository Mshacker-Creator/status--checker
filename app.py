from flask import Flask, request
import os
from datetime import datetime

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return open("index.html").read()

@app.route("/upload", methods=["POST"])
def upload():
    if "photo" in request.files:
        photo = request.files["photo"]
        mobile = request.form.get("mobile", "unknown")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        filename = os.path.join(UPLOAD_FOLDER, f"{mobile}_{timestamp}.png")
        photo.save(filename)
        print(f"✅ Saved: {filename}")
        return "OK", 200
    return "No file", 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)