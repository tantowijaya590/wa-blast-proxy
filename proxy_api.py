from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "🛡️ Proxy Middleware WA aktif bro!"

@app.route('/relay', methods=['POST'])
def relay():
    try:
        data = request.get_json()

        token = data.get("token")
        payload = data.get("payload")

        if not token or not payload:
            return jsonify({"error": "Token dan payload wajib"}), 400

        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

        res = requests.post("https://api.waboxapp.com/send/chat", json=payload, headers=headers)

        return jsonify({
            "status": res.status_code,
            "response": res.text
        }), res.status_code

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
