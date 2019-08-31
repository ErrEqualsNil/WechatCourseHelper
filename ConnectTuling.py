import json
import requests
url = 'http://openapi.tuling123.com/openapi/api/v2'

def postMsg(msg,userid):
    data = {
    "perception": {
        "inputText": {
            "text": msg
            },
        },
    "userInfo": {
        "apiKey": "13b863af214b47a193edb1def5770241",
        "userId": userid
        }
    }
    r = requests.post(url,data=json.dumps(data))
    response = eval(r.text)
    return response['results'][0]['values']['text']
