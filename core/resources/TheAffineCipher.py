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

C_list_keys = ['1','3','5','7','9','11','15','17','19','21','23','25']
C_list_values = ['27','9','21','15','3','19','7','23','11','5','17','25']

def Encrypt(msg,keys):
      is_In_c_d = False
      encrypt_num = []
      new_num = []
      result = []
      for num in C_list_keys:
        if keys[0] % 26 == int(num):
          is_In_c_d = True
        else:
          pass 
      if is_In_c_d:
        for letters in msg:
          for letter in letters.lower():
            encrypt_num.append(alp.get(letter))
        for num in encrypt_num:
          new_num.append(((keys[0]*num) + keys[1]) % 26)
        for num in new_num:
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
        print "\n" + BERR + "Please specify Key A with 1,3,5,7,9,11,15,17,19,21,23,25" + BEND
        return 

def Decrypt(msg,keys):
  c = 0 
  d = 0 
  Cd_list = dict(zip(C_list_keys,C_list_values))
  decrypt_num = []
  new_num = []
  result = []
  for letters in msg:
    for letter in letters.lower():
      decrypt_num.append(alp.get(letter))
  for key,value in Cd_list.iteritems():
    if keys[0] % 26 == int(key):
      c = int(value)
      d = (c * (26 - int(keys[1]))) % 26
  for num in decrypt_num:
    if ((c * num) + d) % 26 == 0:
      new_num.append(26)
    else:
      new_num.append(((c * num) + d) % 26)
  for num in new_num:
    for key,value in alp.iteritems():
        if value == num:
          result.append(key)
  RESULT = ''.join(result)
  print "{}{}{}     Decrypting message please wait....{}".format(CRED,attr(1),CBLINK,CEND)
  time.sleep(4)
  print BOKMSG + ' Decrypt status: SUCCESS' + BEND
  time.sleep(1)
  return RESULT 

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# EOF