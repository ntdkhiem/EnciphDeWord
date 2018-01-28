# -*- coding: utf-8 -*-
import random
import os
import random
#from utils.color import *
import bcolors as b 
from colored import fg,attr 
BBLUE=b.BLUE
BERR=b.ERR
BEND=b.END
BFAIL=b.FAIL
BWARN=b.WARN
BOK=b.OK
BUNDERLINE=b.UNDERLINE
BBMSG=b.BMSG 
BOKMSG=b.OKMSG 
CYELLOW=fg(11)
CWHITE=fg(15)
CGREEN=fg(10)
CORGA=fg(202)
CUNDERLINE=attr(4)
CBLINK=attr(5)
CLIGHTBLUE=fg(45)
CRED=fg(196)
CEND=attr(0)

__author__ = "Khiem Nguyen"
__version__ = 'v1.0' 
def banner_show():
    if os.name=="nt":
	    os.system("cls")
    else:
	    os.system("clear")
    #banner_list = ["banner1.txt","banner2.txt","banner3.txt","banner4.txt","banner5.txt","banner6.txt","banner7.txt","banner8.txt","banner9.txt","banner10.txt"]
    #banner = open(os.path.join("core","resources","Banner",random.choice(banner_list))).read()
    banner = ''''''
    #list = ['skull2','snake','key']
    #with open('banner_'+ random.choice(list) + '.txt','r') as f:
    with open('banner_skull3.txt','r') as f:
        banner = f.read()
        f.close()
    print banner.format(BBLUE=BBLUE,BEND=BEND,BFAIL=BFAIL,BOK=BOK,CYELLOW=CYELLOW,CWHITE=CWHITE,CEND=CEND,CBLINK=CBLINK,author=__author__,version=__version__)                                                                                                                       

banner_show()




