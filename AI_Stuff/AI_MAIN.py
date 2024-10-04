from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Example route to call the Together API
@app.route('/api/chat', methods=['POST'])
def chat_with_together_api(history):
    # Extract API key from environment variables
    api_key = '680762d7c2d1303d84771c96172c803f20f66003d67238d17b9f0b1026e71a64'
    #api_key = os.getenv('TOGETHER_API_KEY')

    if not api_key:
        return jsonify({"error": "API key is missing"}), 400

    # The API endpoint
    url = "https://api.together.xyz/v1/chat/completions"

    # The request payload
    payload = {
        "model":"meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
        "messages":history[-1]
    }

    # The headers, including the API key for authorization
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    try:
        # Make the POST request to the Together API
        response = requests.post(url, headers=headers, json=payload)
        print("Response Status Code:", response.status_code)
        print("Response Data:", response.text)
        response_data = response.json()
        print(response_data)
        content = response_data['choices'][0]['message']['content']

        # Return the response from the Together API as JSON
        return content, response_data.status_code

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)


