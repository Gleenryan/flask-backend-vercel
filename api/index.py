from flask import Flask, jsonify, request, send_from_directory
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "..", "static")

@app.route("/")
def home():
    return jsonify({
        "status": "ok",
        "message": "Flask backend on Vercel 🔥"
    })

@app.route("/image/<filename>")
def get_image(filename):
    return send_from_directory(
        os.path.join(STATIC_DIR, "images"),
        filename
    )

@app.route("/hello")
def hello():
    name = request.args.get("name", "Gleen")
    return jsonify({
        "hello": name
    })