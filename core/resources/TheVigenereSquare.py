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
    with open('./docs/TheVigenereHelper.txt','r') as f:
        info = f.read()
        return info
        f.close()
        
def Encrypt(enc_message,keyword):
    global alp
    global punctuations
    encrypt_num = []
    key_list = keyword * len(enc_message)
    encrypt_key = []
    new_num = []
    result = []
    
    for letter in enc_message:
        encrypt_num.append(alp.get(letter))
    for letter in key_list:
        encrypt_key.append(alp.get(letter))
    for i in range(len(encrypt_num)):
        new_num.append((encrypt_num[i] + encrypt_key[i] - 1) % 26)
    
    for num in new_num:
        if num == 0:
            result.append('Z')
        else:
            for letter,number in alp.iteritems():
                if number == num:
                    result.append(letter.upper())
    RESULT = ''.join(result)
    print "{}{}{}     Encrypting message please wait....{}".format(CRED,attr(1),CBLINK,CEND)
    time.sleep(2)
    print BOKMSG + ' Encrypt status: SUCCESS' + BEND
    time.sleep(1)
    return RESULT 
 
def Decrypt(dec_message,keyword):

    decrypt_num = []
    key_list = keyword * len(dec_message)
    decrypt_key = []
    new_num = []
    result = []
    for letter in dec_message:
        decrypt_num.append(alp.get(letter.lower()))
    for letter in key_list:
        decrypt_key.append(alp.get(letter.lower()))
    for i in range(len(decrypt_num)):
        new_num.append((decrypt_num[i] - decrypt_key[i] + 1) % 26)
    for num in new_num:
        if num == 0:
            result.append('z')
        else:
            for letter,number in alp.iteritems():
                if number == num:
                    result.append(letter)
    RESULT = ''.join(result)
    print "{}{}{}     Decrypting message please wait....{}".format(CRED,attr(1),CBLINK,CEND)
    time.sleep(2)
    print BOKMSG + ' Decrypt status: SUCCESS' + BEND
    time.sleep(1)
    return RESULT 

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
 #EOF