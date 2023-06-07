import requests
import json

# Set up the API endpoint URL
api_url = 'https://api.openai.com/v1/chat/completions'

import os
# Set your OpenAI API key
#export OPENAI_API_KEY=<apki key>
api_key = os.environ.get('OPENAI_API_KEY')

# Set the prompt for the conversation
prompt = 'You: Hello\nAI:'

# Generate a response from the API
def generate_response(prompt):
    headers = {
        'Authorization': 'Bearer ' + api_key,
        'Content-Type': 'application/json'
    }

    data = {
    'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'},
                 {'role': 'user', 'content': prompt}],
    'model': 'gpt-3.5-turbo'
    }


    response = requests.post(api_url, headers=headers, data=json.dumps(data))
    response_json = response.json()
    print(response_json)
    if ('error' in response_json):
        raise requests.exceptions.RequestException(f"bad requets {0}", response_json['error']['code']) 
    return response_json['choices'][0]['message']['content']

# Send a user message and receive a response
def send_message(message):
    prompt = ''
    
    prompt += ' ' + message
    response = generate_response(prompt)
    return response

# Example conversation
conversation = [
    'You: Hello',
    'AI: Hi there! How can I assist you today?',
    'You: Can you tell me a joke?',
    'AI: Sure! Why don’t scientists trust atoms? Because they make up everything!'
]

for message in conversation:
    response = send_message(message)
    print(response)

