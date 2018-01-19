# -*- coding: utf-8 -*-
import random
import os
from utils.color import *
__author__ = "Khiem Nguyen"
__version__ = 'v1.0' 
def banner_show():
    if os.name=="nt":
	    os.system("cls")
    else:
	    os.system("clear")
    banner_list = ["banner1.txt","banner2.txt","banner3.txt","banner4.txt","banner5.txt","banner6.txt","banner7.txt","banner8.txt","banner9.txt","banner10.txt"]
    banner = open(os.path.join("core","resources","Banner",random.choice(banner_list))).read()
    print banner.format(BBLUE=BBLUE,BEND=BEND,BFAIL=BFAIL,BOK=BOK,CYELLOW=CYELLOW,CWHITE=CWHITE,CEND=CEND,CBLINK=CBLINK,author=__author__,version=__version__)                                                                                                                       






