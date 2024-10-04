from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Example route to call the Together API
@app.route('/api/chat', methods=['POST'])
def chat_with_together_api():
    # Extract API key from environment variables
    api_key = os.getenv('TOGETHER_API_KEY')

    if not api_key:
        return jsonify({"error": "API key is missing"}), 400

    # The API endpoint
    url = "https://api.together.xyz/v1/chat/completions"

    # The request payload
    payload = {
        "model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
        "messages": [
            {"role": "user", "content": "What are some fun things to do in New York?"}
        ]
    }

    # The headers, including the API key for authorization
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    try:
        # Make the POST request to the Together API
        response = requests.post(url, headers=headers, json=payload)

        # Return the response from the Together API as JSON
        return jsonify(response.json()), response.status_code

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)


