from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Define your API endpoint and key
TOGETHER_API_URL = "https://api.together.xyz/v1/chat/completions"
TOGETHER_API_KEY = "314c378d4b2f51491df2c6c6a27332b58584e5d7ca928e48be4d97541562109b"  # Replace with your actual API key

@app.route('/chat', methods=['POST'])
def chat():
    # Get the user's input message from the POST request
    user_input = request.json.get("message", "What are some fun things to do in New York?")
    
    # Set up the headers and data for the API request
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
