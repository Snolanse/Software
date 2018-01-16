# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 16:52:48 2018

@author: marius
"""

import requests
requests.packages.urllib3.disable_warnings()

def fåVærData():
    
    URL = "https://feed.metnet.no/current/"
    
    header = {'token': "FeLQrwndUyuE5mRuuPNJ5BifQtCrcO",
              "User-Agent": "Snølanse",
              "Host": "feed.metnet.no",
              "Content-Length": "0"}
    
    minRequest = requests.post(URL,headers=header, verify=False)
    
    return minRequest.json()['data']

