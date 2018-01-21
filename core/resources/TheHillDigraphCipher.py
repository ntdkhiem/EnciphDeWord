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
    with open('./docs/TheHillDigraphHelper.txt','r') as f:
        info = f.read()
        return info
        f.close()

def Encrypt(msg,keys):
    A = keys[0]
    B = keys[1]
    C = keys[2]
    D = keys[3]
    enc_list = [msg[i:i+2] for i in range(0, len(msg), 2)]
    enc_num = []
    new_num = []
    result = []
    determinant = ((A * D) - (B * C)) % 26
    if determinant in C_list:
        for two_letters in enc_list:
          if len(two_letters) == 1:
            enc_list.pop()
            two_letters = two_letters.__add__('x')
            enc_list.append(two_letters)
          enc_num.append([alp.get(letter.lower()) for letter in two_letters])
        for letter_pair in enc_num:
          letter_1 = letter_pair.__getitem__(0)
          letter_2 = letter_pair.__getitem__(1)
          new_letter_1 = ((A * letter_1) + (B * letter_2)) % 26
          new_letter_2 = ((C * letter_1) + (D * letter_2)) % 26
          new_num.append([new_letter_1,new_letter_2])
        for num_pair in new_num:
          for num in num_pair:
            if num == 0:
              result.append('Z')
            else:
              for letter,number in alp.iteritems():
                if number == num:
                      result.append(letter.upper())
        RESULT = ''.join(result)
        print "{}{}{}     Encrypting message please wait....{}".format(CRED,attr(1),CBLINK,CEND)
        time.sleep(4)
        print BOKMSG + ' Encrypt status: SUCCESS' + BEND
        time.sleep(1)
        return RESULT 
    else:
        print "\n" + BERR + "Please use a combination of a,b,c,d that will be 1,3,5,7,9,11,15,17,19,21,23,25" + BEND
        print BERR + '''For example using combination of a,b,c,d that in form of:
              (a=even,b=odd )
              (c=odd ,d=even)''' + BEND
        print "((A * D) - (B * C)) % 26 >> {}: {}BAD{}".format(determinant,CRED,CEND)
        return 




































































#EOF