# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 19:02:38 2018

@author: marius
"""

import tkinter as tk
import time
import lanse

requests.packages.urllib3.disable_warnings()

def tick():
    theLabel.config(text = str(lanse.getSData()['wind']))
    theLabel.after(1000, tick)


root = tk.Tk()
test = 'Nå begynner vi gutta'
theLabel = tk.Label(root, text=test)
theLabel.pack()

tick()


root.mainloop()

