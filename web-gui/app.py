from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL_NAME = "llama3"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message", "").strip()

    if not user_msg:
        return jsonify({"reply": "Please type something 😄"})

    r = requests.post(OLLAMA_URL, json={
        "model": MODEL_NAME,
        "prompt": user_msg,
        "stream": False
    })

    bot_reply = r.json().get("response", "No response")
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
