import requests
import json
import sys
import CucumberJsonReducement


def send_chunks(chunks, api_key):

    # Set up the base URL and headers for the API request
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        #"Authorization": f"Bearer {api_key}",
        "Authorization": f"Bearer " + api_key,
        "Content-Type": "application/json"
    }

    # create all messages
    messages = [{"role": "system", "content": "You are a helpful assistant."}]
    for chunk in chunks:
        messages.append({"role": "user", "content": chunk})

    summarize_question = "I sent you in chunks a json file of my tests, please see it as one big message. can you summarize it? please add the number of failures and success "
    messages.append({"role": "user", "content": summarize_question})


    payload = {"messages": messages,
               'model': 'gpt-3.5-turbo'}
    response = requests.post(url, headers=headers, json=payload)
    data = json.loads(response.text)
    choices = data.get('choices')
    if choices:
        reply = choices[0]['message']['content']
        return reply
    else:
        # Handle the error case here
        return "Oops! Something went wrong."


def create_message_structure(json_path, api_key):

    # Define our JSON payload
    json_payload = json.dumps(CucumberJsonReducement.reduce_json_structure(json_path))

    # Define the maximum chunk size (in characters) for each request
    max_chunk_size = 3000

    # Split the JSON payload into chunks
    chunks = [json_payload[i:i+max_chunk_size] for i in range(0, len(json_payload), max_chunk_size)]
    #print(chunks)

    # Send the chunks to the API and get the response
    response = send_chunks(chunks, api_key)

    # Return the response
    print(response)
    return response




#create_message_structure('/Users/emaximof/Desktop/cucumberWithFailed.json', "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")

if __name__ == '__main__':
  if (len(sys.argv) != 2):
      print("usage: pass two arguments cucamber.json file path, openai apikey")
  json_path = sys.argv[1]
  apikey = sys.argv[2]
  print("calling chatgpt")
  res = create_message_structure(json_path, apikey)
  print(res)




