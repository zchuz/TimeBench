import openai
import os
os.environ['http_proxy'] = 'http://127.0.0.1:7890'
os.environ['https_proxy'] = 'http://127.0.0.1:7890'
openai.api_base = 'https://api.closeai-proxy.xyz/v1'
openai.api_key = 'sk-6N0Ow7FjBtZ7ziQBk2LYtXT4P7KmbJQKmSs0WavLdQCx7H2C'



response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a chatbot"},
        {"role": "user", "content": "Why should DevOps engineer learn kubernetes?"},
    ]
)

print(response)
