import requests

response = requests.get("http://randomfox.ca/floof")
print(response.text)
fox = response.json()
print(fox['link'])
