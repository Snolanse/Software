# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 19:02:38 2018

@author: Marius
"""

import tkinter as tk
import time
import lanse
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def tick():
    theLabel.config(text = str(lanse.getSData()['wind']))
    theLabel.after(1000, tick)


root = tk.Tk()
test = 'Nå begynner vi gutta'
theLabel = tk.Label(root, text=test)
theLabel.pack()

tick()


root.mainloop()

