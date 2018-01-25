# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 19:02:38 2018

@author: Marius
"""

#import tkinter as tk
#
#root = tk.Tk()
#
#topFrame = tk.Frame(root)
#topFrame.pack()
##bottomFrame = tk.Frame(root)
##bottomFrame.pack()
#
#button1 = tk.Button(topFrame, text = 'På', fg = 'red')
#button2 = tk.Button(topFrame, text = 'av', fg = 'red')
#button3 = tk.Button(topFrame, text = 'panikk', fg = 'red')
#
#button1.pack(side='left')
#button2.pack(side='right')
#button3.pack(side='left')
#
#one = tk.Label(root, text="one", bg='black', fg='red')
#one.pack(fill='y')
#
#root.mainloop()

import serial

port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=3.0)

while True:
    rcv = port.read(10)
    port.write("\r\nYou sent:" + repr(rcv))