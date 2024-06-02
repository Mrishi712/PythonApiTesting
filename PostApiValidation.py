import json
import requests
import jsbeautifier

# declaring the values which need to change in payload
name = "Test Book 1"
isbn = "bookcode"
aisle = "17868"
author = "TesterQA"

# POST Call
# declaring url and fetching the payload from json file
url = "https://rahulshettyacademy.com/Library/Addbook.php"
with open('payloads/addBookLibraryPL.json', 'r') as reader:
    payLoad = json.load(reader)
    payLoad["name"] = name
    payLoad["isbn"] = isbn
    payLoad["aisle"] = aisle
    payLoad["author"] = author

req_headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url, headers=req_headers, json=payLoad)
response_body = response.text
print(jsbeautifier.beautify(response_body))
