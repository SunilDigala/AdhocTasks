# Python program to read
# json file

import pandas as pd
import json


# Opening JSON file
f = open('SourceFiles/Expenses.json')

# returns JSON object as
# a dictionary
data = json.load(f)
print(data)

df = pd.json_normalize(data,["WEEK","EXPENSE"],["WHO",["WEEK","NUMBER"]],errors='ignore')
df1 = pd.json_normalize(data,["WEEK","EXPENSE"],[["WEEK","NUMBER"],"WHO"],errors='ignore')
#df1 = pd.json_normalize(data1)
print(df)
print(df1)

#print(df1)
#print(df1.columns)
#type(data)
#print(data[1])
# Iterating through the json
# list
#for i in data:
#	print(i["WHO"])
# Closing file
f.close()
