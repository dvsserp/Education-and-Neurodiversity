from flask import Flask, request, jsonify
import requests
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

# Set up rate limiting (e.g., 5 requests per minute per IP)
limiter = Limiter(get_remote_address, app=app, default_limits=["5 per minute"])

# Example route to call the Together API
@app.route('/api/chat', methods=['POST'])
@limiter.limit("5 per minute")  # Apply rate limiting here
def chat_with_together_api(prompt, history):
    # Extract API key from environment variables
    api_key = '314c378d4b2f51491df2c6c6a27332b58584e5d7ca928e48be4d97541562109b'

    # Extract history from the request
    history = [{"role":"user", "content":prompt}]

    # The API endpoint
    url = "https://api.together.xyz/v1/chat/completions"

    # The request payload
    payload = {
        "model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
        "messages": history
    }

    # The headers, including the API key for authorization
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    try:
        # Make the POST request to the Together API
        response = requests.post(url, headers=headers, json=payload)
        response_data = response.json()
        print(response_data)
        content = response_data['choices'][0]['message']['content']

        # Return the response from the Together API as JSON
        return content
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
