import json

import requests
import jsbeautifier

# GET Call
# declaring url and params
url = "https://rahulshettyacademy.com/Library/GetBook.php"
author = 'Devil'
parameters = {"AuthorName": author}

# Hitting the GET request
response = requests.get(url, params=parameters)

# Fetching the response status code
responseStatusCode = response.status_code

# Fetching the response body & printing in beautified
responseBody = response.text
print(jsbeautifier.beautify(responseBody))

if responseStatusCode == 200:
    # convert the response into a dict from string
    print(type(responseBody))
    dict_responseBody = json.loads(responseBody)
    print(type(dict_responseBody))

    # Check all isbn is of same type
    for books in dict_responseBody:
        if books["isbn"] == "sdfgrfyh":
            print("ISBN : is same as sdfgrfyh")

    # Number of book written
    print("Number of Books : ", len(dict_responseBody))
else:
    assert responseStatusCode == 404
    print(responseStatusCode)

# Fetching the response headers
responseHeaders = response.headers
print(responseHeaders["Content-Type"])
