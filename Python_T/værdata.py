# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 16:52:48 2018

@author: marius
"""

import requests
requests.packages.urllib3.disable_warnings()
import numpy

def fåVærData():
    """Henter data fra værstasjon via server"""
    URL = "https://feed.metnet.no/current/"
    
    header = {'token': "FeLQrwndUyuE5mRuuPNJ5BifQtCrcO",
              "User-Agent": "Snølanse",
              "Host": "feed.metnet.no",
              "Content-Length": "0"}
    
    minRequest = requests.post(URL,headers=header, verify=False)
    
    return minRequest.json()['data']

def wetbulb(temp,hum):
    """rekner ut wet-bulb tempratur ut fra lufttempratur og luftfuktighet""" 
    wbulb = (20*numpy.arctan(0.151977*(hum + 8.313659)**0.5)
            + numpy.arctan(temp + hum)
            - numpy.arctan(hum - 1.676331)
            + 0.00391838*hum**(3/2)*numpy.arctan(0.023101*hum)
            - 4.686035)
    
    wbulb = round(float(wbulb),1)
    
    return wbulb
