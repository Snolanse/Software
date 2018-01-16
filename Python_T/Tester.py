# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 19:02:38 2018

@author: marius
"""

import værdata
import time
import random
t = 0
for x in range(0,30):
    t0 = time.time()
    import requests
    T = værdata.fåVærData()
    t = t + time.time() - t0
    time.sleep(random.random()*3)
print(t/30)
