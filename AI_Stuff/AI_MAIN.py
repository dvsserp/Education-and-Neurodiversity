from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Example route to call the Together API
@app.route('/api/chat', methods=['POST'])
def chat_with_together_api(query):
    '''
    # Extract API key from environment variables
    api_key = '314c378d4b2f51491df2c6c6a27332b58584e5d7ca928e48be4d97541562109b'
    #api_key = os.getenv('TOGETHER_API_KEY')

    if not api_key:
        return jsonify({"error": "API key is missing"}), 400

    # The API endpoint
    url = "https://api.together.xyz/v1/chat/completions"

    # The request payload
    payload = {
        "model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
        "messages": [
            {"role": "user", "content": query}
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
    '''
    return "This is the responce"
if __name__ == '__main__':
    app.run(debug=True)


