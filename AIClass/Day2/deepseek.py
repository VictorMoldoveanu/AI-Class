import aicamp_day1
import os
import requests

API_URL = "https://router.huggingface.co/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {os.environ['HF_TOKEN']}",
}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

response = query({
    "messages": [
        {
            "role": "user",
            "content": "What is the indefinate integral of x/(x+1)"
        }
    ],
    "model": "deepseek-ai/DeepSeek-R1:novita"
})

text = aicamp_day1.make_text(response)
print(text)