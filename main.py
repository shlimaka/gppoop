import os
import requests
import json

OPENAI_API_KEY=(os.environ['OPENAI_API_KEY'])
PROMT=input("Ask gppoop about something: ")
MODEL=("gpt-3.5-turbo")
API_URL=("https://api.openai.com/v1/chat/completions")

payload = {
    "model": MODEL,
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
data = response.json()

if response.status_code == 200:
    get_answer = data['choices'][0]['message']['content']
    formatted_get_answer = "\033[34m" + get_answer + "\033[0m"

    print(formatted_get_answer)
else:
    print("Error:", response.status_code)
    print(response.text)

if response.status_code == 200:
    get_usage = data['usage']['prompt_tokens'], data['usage']['completion_tokens'], data['usage']['total_tokens']

    formatted_usage = (
    "\033[33m| Prompt tokens: " + str(get_usage[0]) +
    " | Completion tokens: " + str(get_usage[1]) +
    " | Total tokens: " + str(get_usage[2]) + "\033[0m"
    )

    print("\n" + formatted_usage)