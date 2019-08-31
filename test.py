path = "./classes.json"
import json
with open (path,'r') as f:
    dict = json.load(f)
    for key,value in dict.items():
        print(key)
        for each in value:
            print(each)