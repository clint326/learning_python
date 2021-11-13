# first import the library that will allow us to do API requests
import requests

# next make a simple call to the Random Fox api
response = requests.get("http://randomfox.ca/floof")

# next print the response as text and as json
print(response.text)
print (response.json())

# next assign variable 'fox' to the json output and print the image URL
fox = response.json()
print(fox['image'])
