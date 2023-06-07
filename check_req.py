import requests

url = 'http://example.com'
response = requests.post(url)

if response.status_code == 200:
    print('Request was successful!')
else:
    print('An error occurred with status code:', response.status_code)
