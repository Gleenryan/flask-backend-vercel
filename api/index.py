from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "status": "ok",
        "message": "Flask backend on Vercel 🔥"
    })

@app.route("/hello")
def hello():
    name = request.args.get("name", "Gleen")
    return jsonify({
        "hello": name
    })
