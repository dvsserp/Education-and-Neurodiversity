import requests
import json

def make_post_request(api_key):
    url = "https://api.together.xyz/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
        "messages": [
            {"role": "user", "content": "What are some fun things to do in New York?"}
        ]
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code} - {response.text}"

# Replace with your API key
api_key = "680762d7c2d1303d84771c96172c803f20f66003d67238d17b9f0b1026e71a64"
response = make_post_request(api_key)
print(response)