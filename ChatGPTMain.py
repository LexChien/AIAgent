import openai
import requests
import os

api_key = os.getenv("OPENAI_API_KEY")
if api_key is None:
    raise ValueError("The API key is not set. Please set the OPENAI_API_KEY environment variable.")

response = requests.post(
    'https://api.openai.com/v1/chat/completions',
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    },
    json = {
        'model': 'gpt-4o',
        'messages': [
                {'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': 'who are you?'}
        ],
        'temperature': 0.4,
        'max_tokens': 300
    })

json = response.json()
print(json)