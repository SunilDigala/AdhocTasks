# Python program to read
# json file


import json

# Opening JSON file
f = open('SourceFiles/Expenses.json')

# returns JSON object as
# a dictionary
data = json.load(f)

type(data)
print(data[1])
# Iterating through the json
# list
for i in data:
	print(i["WHO"])
# Closing file
f.close()
