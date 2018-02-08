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

#"{0:b}".format(binær) blir binær string
# int(binærstring,2) blir tall


import serial
import time

sd = [b"\x48",b"\x45",b"\x49",b"\x5c",b"\x6e",b"\x5c",b"\x72"]
ser = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=0)

while True:
#    rcv = ser.read(100)
#    print(rcv)
    for x in sd:
        ser.write(x)
    
#    ser.write(b"\x48")
#    ser.write(b"\x45")
#    ser.write(b"\x49")
#    ser.write(b"\x5c")
#    ser.write(b"\x6e")
#    ser.write(b"\x5c")
#    ser.write(b"\x72")
#    ser.write(b"\x72")
    time.sleep(3)
#    try:
#        for x in rcv:
#            print("{0:b}".format(x))
#    except:
#        print("nogo")
