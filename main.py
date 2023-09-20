import os
import requests
import json

OPENAI_API_KEY=(os.environ['OPENAI_API_KEY'])
PROMT=input("Ask GpPoop about somethink: ")
API_URL=("https://api.openai.com/v1/chat/completions")

payload = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": PROMT}
    ]
}

headers = {
    "Authorization": f"Bearer {OPENAI_API_KEY}",
    "Content-Type": "application/json"
}

response = requests.post(API_URL, data=json.dumps(payload), headers=headers)

if response.status_code == 200:
    data = response.json()   
    gpt_answer = data['choices'][0]['message']['content']

    print(gpt_answer)
else:
    print("Error:", response.status_code)
    print(response.text)