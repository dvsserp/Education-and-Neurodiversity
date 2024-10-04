from flask import Flask, request, jsonify
import requests
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

limiter = Limiter(get_remote_address, app=app, default_limits=["5 per minute"])


@app.route('/api/chat', methods=['POST'])
@limiter.limit("5 per minute")  # Apply ate limiting here
def chat_with_together_api(prompt, history):

    api_key = '314c378d4b2f51491df2c6c6a27332b58584e5d7ca928e48be4d97541562109b'

    history.append({"role":"user", "content":prompt})

    url = "https://api.together.xyz/v1/chat/completions"

    payload = {
        "model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
        "messages": history
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response_data = response.json()
        print(response_data)
        content = response_data['choices'][0]['message']['content']
        history.append({"role":"assistant", "content":content})
        return content, history
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
