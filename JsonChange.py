import json
def read(path):
     with open (path,'r') as f:
        dict = json.load(f)
        return dict

def change(path,dict):
    with open (path,'w') as f:
        json.dump(dict,f)