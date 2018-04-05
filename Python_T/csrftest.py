import requests
import json

def serverCom(bronnid, get, data):

    url1 = "http://127.0.0.1:8000"
    url2 = "http://127.0.0.1:8000/test"
    client = requests.session()
    client.get(url1)
    csrftoken = client.cookies['csrftoken']

    l_data = dict(csrfmiddlewaretoken=csrftoken, bronnid=bronnid, get = get, next='/')

    r = client.post(url2, data=l_data, headers=dict(Referer=url2))
    return(json.loads(r.content.decode()))