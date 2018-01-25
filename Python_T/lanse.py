# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 16:52:48 2018

@author: marius
"""

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import numpy
import time

def getSData():
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
    wbulb = (temp*numpy.arctan(0.151977*(hum + 8.313659)**0.5)
            + numpy.arctan(temp + hum)
            - numpy.arctan(hum - 1.676331)
            + 0.00391838*hum**(3/2)*numpy.arctan(0.023101*hum)
            - 4.686035)
    
    wbulb = round(float(wbulb),1)
    
    return wbulb

class PI:
    """Pi regulator"""
    
    def __init__(self,P,I):
        
        self.Kp = P
        self.Ti = I
        
        self.sample_time = 0.00
        self.current_time = time.time()
        self.last_time = self.current_time
        
        self.clear()
        
    def clear(self):
        """sletter utrekninger"""
        
        self.setpoint = 0.0
        
        self.PTerm = 0.0
        self.TiTerm = 0.0
        self.last_error = 0.0
        
        #antiwindup
        self.int_error = 0.0
        self.antiwindup = 20.0
        
        self.output = 0.0
        
    def update(self, feedback):
        """Rekner ut PI verdien etter referansen
        
        Matte: u(t) = K_p e(t) + K_i \int_{0}^{t} e(t)dt"""
        
        error = self.setpoint - feedback
        
        self.current_time = time.time()
        delta_time = self.current_time - self.last_time
        
        if (delta_time >= self.sample_time):
            self.PTerm = self.Kp * error
            self.TiTerm += error * delta_time
            
            if (self.TiTerm < -self.antiwindup):
                self.TiTerm = -self.antiwindup
            elif (self.TiTerm > self.antiwindup):
                self.TiTerm = self.antiwindup
            
            #Lagrer forrige verdier
            self.last_time = self.current_time
            self.last_error = error
            
            self.output = self.PTerm + (self.Ti * self.TiTerm)
            
    def setRef(self,referanse):
        """Setter ønsket referanseverdi"""
        self.setpoint = referanse
    
    def setKp(self, proportional_gain):
        """setter hvor hardt regulatoren skal reagere på avvik"""
        self.Kp = proportional_gain
        
    def setTi(self, integral_gain):
        """setter hvor hardt regulatoren skal reagere på avvik over tid"""
        self.Ti = integral_gain
    
    def setAntiwindup(self, integral_limit): #Feil her
        """setter grenser på hvor mye regulatoren kan integrere seg opp"""
        self.antiwindup = integral_limit
        
    def setSampleTime(self, sample_time):
        """Setter hvor ofte regulatoren skal oppdatere seg"""
        self.sample_time = sample_time
