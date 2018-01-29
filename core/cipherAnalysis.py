#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division
import string
import random
from utils.color import *

def Analysis(cipherText):
    nums_0 = (0 for i in range(27))
    alp = dict(zip(string.ascii_lowercase,nums_0))
    for letter in Cipher:
        for key,value in alp.iteritems():
            if letter == key:
                alp[key] += 1
    for key,value in alp.iteritems():
        alp[key] = value * (value - 1)
    IC = sum(alp.values()) / (len(cipherText) * len(cipherText) - 1)
    key_len = ((0.027 * len(cipherText)) / (len(cipherText) - 1) * IC - 0.038 * len(cipherText) + 0.065)
    # if IC > 0.06:
    #     if IC > 0.052:
    #         prit "More likely monoalphabetic"
    #     else:
    #         print "Probably monoalphabetic"
    # elif IC < 0.045:
    #     print "{}".format(random.choice(["More likely polyalphabetic","Probably polyalphabetic"]))
    # print " The one below is the prediction of key length that onl for TheVigenereSquare cipher"
    # print "%.6f" % abs(key_len)
    return IC,key_len

def handler():
    cText = ''
    IC = 0
    mono_poly = ''
    while True:
            cmd_ = raw_input("{}{}(CipherAnalysis){} >> ".format(BUNDERLINE,BBLUE,BEND)).strip()
            if cmd_ == 'help' or cmd_ == 'h' or cmd_ == '?':
                help_ = helper.help_('analysis','')
                print help_.format(CLIGHTBLUE,CEND)
            elif cmd_.startswith('show') and cmd_encrypt.endswith('info'):
                if __platform__.startswith('Linux') or __platform__.startswith('Darwin'):
                    header = ['Type','Result','Description']
                    rows = [['Cipher Text',cText,'Encrypted message'],
                            ['Incidence of Coincidence',IC,'Incidenc of Coincidence of prediction'],
                            ['Result',mono_poly,'Prediction whether monoalphabetic or polyalphabetic'],
                            ['']]
