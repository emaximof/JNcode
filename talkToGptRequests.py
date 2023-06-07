import requests
import json


#export OPENAI_API_KEY=<apki key>
api_key = os.environ.get('OPENAI_API_KEY')

url = "https://api.openai.com/v1/chat/completions"
headers = {
    'Authorization': 'Bearer ' + api_key,
    "Content-Type": "application/json"
}

def chat_with_gpt(prompt):
    payload = {
        "messages": [{"role": "system", "content": "You are a helpful assistant."},
                     {"role": "user", "content": prompt}],
        'model': 'gpt-3.5-turbo'
    }
    response = requests.post(url, headers=headers, json=payload)
    data = json.loads(response.text)
    choices = data.get('choices')
    if choices:
        reply = choices[0]['message']['content']
        return reply
    else:
        # Handle the error case here
        return "Oops! Something went wrong."



user_input = "Hello, how are you?"
response = chat_with_gpt(user_input)
print(response)


