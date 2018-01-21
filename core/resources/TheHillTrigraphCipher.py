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
        
def Encrypt(msg,keys):
  A = keys[0]
  B = keys[1]
  C = keys[2]
  D = keys[3]
  E = keys[4]
  F = keys[5]
  G = keys[6]
  H = keys[7]
  I = keys[8]
  enc_list = [msg[i:i+3] for i in range(0, len(msg), 3)]
  enc_num = []
  new_num = []
  result = []
  determinant = ((A * E * I) - (A * F * H) - (D * B * I) + (D * C * H) + (G * B * F) - (G * C * E)) % 26
  if determinant in C_list:
    for three_letters in enc_list:
      if len(three_letters) == 1:
        enc_list.pop()
        three_letters = three_letters.__add__('xx')
        enc_list.append(three_letters)
      elif len(three_letters) == 2:
        enc_list.pop()
        three_letters = three_letters.__add__('x')
        enc_list.append(three_letters)
      enc_num.append([alp.get(letter.lower()) for letter in three_letters])
    for letter_pair in enc_num:
      letter_1 = letter_pair.__getitem__(0)
      letter_2 = letter_pair.__getitem__(1)
      letter_3 = letter_pair.__getitem__(2)
      new_letter_1 = ((A * letter_1) + (B * letter_2) + (C * letter_3)) % 26
      new_letter_2 = ((D * letter_1) + (E * letter_2) + (F * letter_3)) % 26
      new_letter_3 = ((G * letter_1) + (H * letter_2) + (I * letter_3)) % 26
      if new_letter_1 == 0:
        new_letter_1 = 26
      elif new_letter_2 == 0:
        new_letter_2 = 26
      elif new_letter_3 == 0:
        new_letter_3 = 26
      new_num.append([new_letter_1,new_letter_2,new_letter_3])
    for num_pair in new_num:
      for num in num_pair:
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
    print "\n" + BERR + "Please use a combination of A,B,C,D,E,F,G,H,I that will be 1,3,5,7,9,11,15,17,19,21,23,25" + BEND
    print BERR + '''Try using those keys in form of:
      (a = ODD ,b = ODD,c = EVEN)    (a = EVEN,b = ODD,c = ODD )
      (d = EVEN,e = ODD,f = EVEN) or (d = EVEN,e = ODD,f = ODD )
      (g = EVEN,h = ODD,i = ODD )    (g = ODD ,h = ODD,i = ODD )\n''' + BEND
    print "((A * E * I) - (A * F * H) - (D * B * I) + (D * C * H) + (G * B * F) - (G * C * E)) % 26 >> {}: {}BAD{}".format(determinant,CRED,CEND)
    return 
    
def Decrypt(msg,keys):
  A = keys[0]
  B = keys[1]
  C = keys[2]
  D = keys[3]
  E = keys[4]
  F = keys[5]
  G = keys[6]
  H = keys[7]
  I = keys[8]
  dec_list = [msg[i:i+3] for i in range(0, len(msg), 3)]
  dec_num = []
  new_num = []
  result = []
  determinant = ((A * E * I) - (A * F * H) - (D * B * I) + (D * C * H) + (G * B * F) - (G * C * E)) % 26
  inverse_determinant = 0
  if determinant in C_list:
    for key,value in C_list.iteritems():
      if determinant == key:
        inverse_determinant = value
    new_A = ((((E * I) - (F * H))  % 26) * inverse_determinant) % 26
    new_B = ((((C * H) - (B * I)) % 26) * inverse_determinant ) % 26
    new_C = ((((B * F) - (C * E)) % 26) * inverse_determinant) % 26
    new_D = ((((F * G) - (D * I)) % 26) * inverse_determinant) % 26
    new_E = ((((A * I) - (C * G)) % 26) * inverse_determinant) % 26
    new_F = ((((C * D) - (A * F)) % 26) * inverse_determinant) % 26
    new_G = ((((D * H) - (E * G)) % 26) * inverse_determinant) % 26
    new_H = ((((B * G) - (A * H)) % 26) * inverse_determinant) % 26
    new_I = ((((A * E) - (B * D)) % 26) * inverse_determinant) % 26
    for three_letters in dec_list:
      dec_num.append([alp.get(letter.lower()) for letter in three_letters])
    for letter_pair in dec_num:
      letter_1 = letter_pair.__getitem__(0)
      letter_2 = letter_pair.__getitem__(1)
      letter_3 = letter_pair.__getitem__(2)
      new_letter_1 = ((new_A * letter_1) + (new_B * letter_2) + (new_C * letter_3)) % 26
      new_letter_2 = ((new_D * letter_1) + (new_E * letter_2) + (new_F * letter_3)) % 26
      new_letter_3 = ((new_G * letter_1) + (new_H * letter_2) + (new_I * letter_3)) % 26
      if new_letter_1 == 0:
        new_letter_1 = 26
      elif new_letter_2 == 0:
        new_letter_2 = 26
      elif new_letter_3 == 0:
        new_letter_3 = 26
      new_num.append([new_letter_1,new_letter_2,new_letter_3])
    for num_pair in new_num:
      for num in num_pair:
        for letter,number in alp.iteritems():
          if number == num:
                result.append(letter)
    if result[-1] == 'x' and result[-2] == 'x':
      result.pop()
      result.pop()
    elif result[-1] == 'x':
      result.pop()
    RESULT = ''.join(result)
    print "{}{}{}     Decrypting message please wait....{}".format(CRED,attr(1),CBLINK,CEND)
    time.sleep(4)
    print BOKMSG + ' Decrypt status: SUCCESS' + BEND
    time.sleep(1)
    return RESULT 
  else:
    return
    
    
    
    
    
    
    
    
    
    
    
    
    
#EOF