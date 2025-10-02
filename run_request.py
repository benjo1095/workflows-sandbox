"""
Runs a simple requests example

"""

import requests


print("Making a request to example.com...")
url = "https://www.example.com"
response = requests.get(url)
print(f"Response status code: {response.status_code}")
print(f"Response content: {response.text[:100]}")  
print("Request completed.")

