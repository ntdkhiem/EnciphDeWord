from os import path
from random import choice
from core.color import CYAN, GREEN, RED, RESET

def banner():
    banner_list = ["banner_1.txt","banner_2.txt","banner_3.txt","banner_4.txt","banner_5.txt","banner_6.txt","banner_7.txt","banner_8.txt"]
    banner = open(path.join("core","banner", choice(banner_list))).read()
    print (banner.format(cyan=CYAN, green=GREEN, red=RED, reset=RESET))