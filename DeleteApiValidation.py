import json
import requests
import jsbeautifier

# declaring the replacing values which need to change in payload
bookID = "sdfgrfyh67"
delete_payload = '{"ID": "bookID"}'
newPayload = delete_payload.replace("bookID", bookID)

# Load method and parse json and its returns dictnory
dict_delete_payload = json.loads(newPayload)
print(dict_delete_payload)

# DELETE Call
# declaring url and fetching the payload from json file
url = "https://rahulshettyacademy.com/Library/DeleteBook.php"
req_headers = {
    'Content-Type': 'text/plain'
}

response = requests.post(url, headers=req_headers, json=dict_delete_payload)
response_body = response.text
print(jsbeautifier.beautify(response_body))
dict_response_body = json.loads(response_body)
print(dict_response_body['msg'])

# assert for both 404 and 200
if response.status_code == 200:
    assert dict_response_body['msg'] == "book is successfully deleted"
    print('200')
else:
    assert dict_response_body['msg'] == "Delete Book operation failed, looks like the book doesnt exists"
    print('404')
