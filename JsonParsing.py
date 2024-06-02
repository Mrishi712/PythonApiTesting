import json

myData = '{"name" : "API Testing","languages":["java","javascript","python"]}'

# Load method and parse json and its returns dictnory
dict_myData = json.loads(myData)
print(type(dict_myData))
print(dict_myData)
print(dict_myData["languages"])
print(type(dict_myData["languages"]))
languagesAvailable = dict_myData["languages"]
firstLanguage = languagesAvailable[0]
print(firstLanguage)
for language in languagesAvailable:
    print(language)