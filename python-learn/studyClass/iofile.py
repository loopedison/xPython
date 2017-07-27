#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import types
import time
from datetime import datetime
import random

print ('\r>>>====================================<<<')
print (time)
print (dir(time))
print (random)
print (dir(random))

print ('\r>>>====================================<<<')
log = open('log.txt','w')
for x in range(1,10):
    now = str(datetime.now())
    data = random.randint(0,1024)
    log.write(now+'==='+str(data)+'\n')
    time.sleep(0.2)
    print (x*'.')
    pass
log.flush()
log.close()

print ('\r>>>====================================<<<')


print (os.environ)
