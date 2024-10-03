from flask import Flask, request, jsonify
import requests
import os 

app = Flask(__name__)

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

TOGETHER_API_URL = "https://api.together.xyz/v1/chat/completions"

@app.route('/chat', methods=['POST'])
def chat():
    if not TOGETHER_API_KEY:
        return jsonify({"error": "API key not set"}), 500
    
    user_input = request.json.get("message", "What are some fun things to do in New York?")
    
    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
        "messages": [
            {"role": "user", "content": user_input}
        ]
    }

    # Make the POST request to the Together API
    response = requests.post(TOGETHER_API_URL, headers=headers, json=data)

    # Return the API response to the Flask user
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)

