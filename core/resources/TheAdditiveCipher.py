#!/usr/bin/python

import string 
import os 
import time
from utils.color import *
from colored import attr
info = []

with open('./core/alphabet.txt','r') as f:
    for line in f.readlines():
        info.append(line.replace('\n',''))
    f.close()
alp = dict(zip(info[0],range(1,27)))
punctuations = info[1]

def info():
    with open('./docs/TheAdditiveHelper.txt','r') as f:
        info = f.read()
        return info
        f.close()

def Encrypt(msg,key):
    global alp
    global punctuations
    
    encrypt_num = []
    new_num = []
    result = []
    for letters in msg:
      for letter in letters.lower():
        if letter in punctuations or letter == ' ':
          encrypt_num.append(letter)
          pass 
        encrypt_num.append(alp.get(letter))
    for num in filter(None,encrypt_num):
      if str(num) in punctuations:
        new_num.append(str(num))
      elif num == ' ':
        new_num.append(num)
      else:
        new_num.append(num + key)
    for num in new_num:
      if str(num) in punctuations:
        result.append(str(num))
      elif num == ' ':
        result.append(num)
      else:
        for letter,number in alp.iteritems():
          if num > 26:
            num = num - 26
            if number == num:
              result.append(letter.upper())
          else:
            if number == num:
              result.append(letter.upper())
    RESULT = ''.join(result)
    print "{}{}{}     Encrypting message please wait....{}".format(CRED,attr(1),CBLINK,CEND)
    time.sleep(4)
    print BOKMSG + ' Encrypt status: SUCCESS' + BEND
    time.sleep(1)
    return RESULT 
    
def Decrypt(enc_msg,key):
    decrypt_num = []
    new_num = []
    result = []
    for letters in enc_msg:
      for letter in letters.lower():
        if letter in punctuations or letter == ' ':
          decrypt_num.append(letter)
          pass 
        decrypt_num.append(alp.get(letter))
    for num in filter(None,decrypt_num):
      if str(num) in punctuations:
        new_num.append(str(num))
      elif num == ' ':
        new_num.append(num)
      else:
        if (key - num) < 0:
          new_num.append(num - key)
        else:
          new_num.append((num - key) + 26)
    for num in new_num:
      if str(num) in punctuations:
        result.append(str(num))
      elif num == ' ':
        result.append(num)
      else:
        for key,value in alp.iteritems():
            if value == num:
              result.append(key)
    RESULT = ''.join(result)
    print "{}{}{}     Decrypting message please wait....{}".format(CRED,attr(1),CBLINK,CEND)
    time.sleep(2)
    print BOKMSG + ' Decrypt status: SUCCESS' + BEND
    time.sleep(1)
    return RESULT 
