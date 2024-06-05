import json
import requests
import jsbeautifier

# POST - Create a Book
name = "Test Book 2"
isbn = "sdfgrfyh"
aisle = "89723"
author = "TesterQA"

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
dict_response_body = json.loads(response_body)
bookCreated = dict_response_body['ID']
print("Book ID created : ",bookCreated)

# GET - Get by Author
url = "https://rahulshettyacademy.com/Library/GetBook.php"
parameters = {"AuthorName": author}

response = requests.get(url, params=parameters)

# Fetching the response body & printing in beautified
responseBody = response.text
responseStatusCode = response.status_code
if responseStatusCode == 200:
    # convert the response into a dict from string
    dict_responseBody = json.loads(responseBody)

    for books in dict_responseBody:
        if books["isbn"] == "sdfgrfyh":
            print("ISBN : is same as sdfgrfyh")
    print("Number of Books : ", len(dict_responseBody))
else:
    assert responseStatusCode == 404
    print(responseStatusCode)

# declaring the replacing values which need to change in payload
delete_payload = '{"ID": "bookID"}'
newPayload = delete_payload.replace("bookID", bookCreated)

# Load method and parse json and its returns dictnory
dict_delete_payload = json.loads(newPayload)

# DELETE Call
# declaring url and fetching the payload from json file
url = "https://rahulshettyacademy.com/Library/DeleteBook.php"
req_headers = {
    'Content-Type': 'text/plain'
}

response = requests.post(url, headers=req_headers, json=dict_delete_payload)
response_body = response.text
dict_response_body = json.loads(response_body)
print(dict_response_body['msg'])

# assert for both 404 and 200
if response.status_code == 200:
    assert dict_response_body['msg'] == "book is successfully deleted"
    print('200')
else:
    assert dict_response_body['msg'] == "Delete Book operation failed, looks like the book doesnt exists"
    print('404')
