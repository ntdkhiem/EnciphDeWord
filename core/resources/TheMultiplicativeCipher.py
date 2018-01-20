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
punctuations = info[1]

def info():
    help_ = ''
    with open('./docs/TheMultiplicativeHelper.txt','r') as f:
        return f.read()
        f.close()


def Encrypt(msg,key):
    global alp
    global punctuations
    if not key in C_list:
        print BERR + "Please give key that's between {0}1,3,5,7,9,11,15,17,19,21,23,25{1}".format(CLIGHTBLUE,CEND)
        return ''
    # static variables
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
        new_num.append(num * key)
    for num in new_num:
      if str(num) in punctuations:
        result.append(str(num))
      elif num == ' ':
        result.append(num)
      else:
        for letter,number in alp.iteritems():
          if num > 26:
            num = num % 26
            if num == 0:
                num = 26
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
    inverse_key = [value for keys,value in C_list.iteritems() if keys == key]
    decrypt_num = []
    new_num = []
    result = []
    for letters in enc_msg:
      for letter in letters.lower():
        if letter in punctuations or letter == ' ':
          decrypt_num.append(letter)
          pass 
        decrypt_num.append(alp.get(letter))
    for num in decrypt_num:
      if str(num) in punctuations:
        new_num.append(str(num))
      elif num == ' ':
        new_num.append(num)
      elif num == 0:
        new_num.append(26)
      else:
            new_num.append((num * inverse_key[0]) % 26)
    for num in new_num:
      if str(num) in punctuations:
        result.append(str(num))
      elif num == ' ':
        result.append(num)
      else:
        for key,value in alp.iteritems():
          if num > 26:
            num = num % 26
            if num == 0:
              num = 26
            if value == num:
              result.append(key)
          else:
            if value == num:
              result.append(key)
    RESULT = ''.join(result)
    print "{}{}{}     Decrypting message please wait....{}".format(CRED,attr(1),CBLINK,CEND)
    time.sleep(2)
    print BOKMSG + ' Decrypt status: SUCCESS' + BEND
    time.sleep(1)
    return RESULT 
