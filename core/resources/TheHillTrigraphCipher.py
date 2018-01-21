#!/usr/bin/python

import string 
import os 
import time
from utils.color import *
from colored import attr
info = []
C_list = {1:27,3:9,5:21,7:15,9:3,11:13,15:7,17:23,19:11,21:5,23:17,25:25}
with open('./core/alphabet.txt','r') as f:
    for line in f.readlines():
        info.append(line.replace('\n',''))
    f.close()
alp = dict(zip(info[0],range(1,27)))

def info():
    with open('./docs/TheHillTrigraphHelper.txt','r') as f:
        info = f.read()
        return info
        f.close()