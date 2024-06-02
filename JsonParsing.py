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
secondLanguage = dict_myData["languages"][1]
print(firstLanguage)
print(secondLanguage)
for language in languagesAvailable:
    print(language)

# parsing json from external file

with open('SampleTestData/sampleJson.json', 'r') as reader:
    currentContent = json.load(reader)
    batters = currentContent["batters"]["batter"]
    print(batters)
    print(type(batters))
    for idName in batters:
        print(idName["type"])
