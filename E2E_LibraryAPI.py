import json
import requests
import configparser

from utilities.payloads import *
from utilities.resources import *
from utilities.testData import *

# Configuring the ini file
config = configparser.ConfigParser()
config.read('utilities/properties.ini')

# Test data for creating the book
name = TestData.name
isbn = TestData.isbn
aisle = TestData.aisle
author = TestData.author

# POST - add book to library
post_api_url = config['API']['baseEndpoint'] + ApiResources.addBook
body = addBookPayload(name, isbn, aisle, author)
req_headers = {
    'Content-Type': 'application/json'
}

response = requests.post(post_api_url, headers=req_headers, json=body)

response_body = response.text
dict_response_body = json.loads(response.text)
bookCreated = dict_response_body['ID']
print("Book ID created : ", bookCreated)

# GET - Get by Author
get_api_url = config['API']['baseEndpoint'] + ApiResources.getBook
parameters = {"AuthorName": author}

response = requests.get(get_api_url, params=parameters)

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

# POST - Delete the book created

# declaring url and fetching the payload from json file
delete_api_url = config['API']['baseEndpoint'] + ApiResources.deleteBook
req_headers = {
    'Content-Type': 'text/plain'
}
delete_payload = deleteBookPayload(bookCreated)

response = requests.post(delete_api_url, headers=req_headers, json=delete_payload)

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
