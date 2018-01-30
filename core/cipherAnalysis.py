#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division
import string
import random
import platform 
from colortable import table
from prettytable import PrettyTable
from utils.color import *
from docs import helper

__platform__ = platform.platform()

def Analysis(cipherText):
    nums_0 = (0 for i in range(27))
    alp = dict(zip(string.ascii_uppercase,nums_0))
    for letter in cipherText:
        for key,value in alp.iteritems():
            if letter == key:
                alp[key] += 1
    header = ['Letter','Repeat Time']
    rows = []
    for i in string.ascii_uppercase:
      rows += [[i,str(alp.get(i)) + '      ']]
    table_maker = table(rows,header,colorfmt='green')
    print table_maker
    for key,value in alp.iteritems():
        alp[key] = value * (value - 1)
    IC = sum(alp.values()) / (len(cipherText) * len(cipherText) - 1)
    key_len = abs(((0.027 * len(cipherText)) / (len(cipherText) - 1) * IC - 0.038 * len(cipherText) + 0.065))
    IC = "%.6f" % IC
    key_len = "%.2f" % key_len
    return IC,key_len



def handler():
    cText = ''
    IC = 0
    mono_poly = ''
    key_len = 0 
    while True:
            cmd_ = raw_input("{}{}(CipherAnalysis){} >> ".format(BUNDERLINE,BBLUE,BEND)).strip()
            if cmd_ == 'help' or cmd_ == 'h' or cmd_ == '?':
                help_ = helper.help_('analysis','')
                print help_.format(CLIGHTBLUE,CEND)
            elif cmd_.startswith('show') and cmd_.endswith('info'):
                if __platform__.startswith('Linux') or __platform__.startswith('Darwin'):
                    header = ['Type','Result','Description']
                    rows = [['Cipher Text',cText,'Encrypted message'],
                            ['Incidence of Coincidence',IC,'Incidence of Coincidence prediction'],
                            ['Result',mono_poly,'Prediction whether monoalphabetic or polyalphabetic'],
                            ['Key length',key_len,'Key length prediction for TheVigenereSquare cipher only']]
                    print
                    print table(rows,header,colorfmt='red')
                    print
                else:
                    table_maker = PrettyTable()
                    table_maker.title = "Information Box"
                    table_maker.field_names = ["Type", "Result","Description"]
                    table_maker.add_row(['Cipher Text',cText,'Encrypted message'])
                    table_maker.add_row(['Incidence of Coincidence',IC,'Incidence of Coincidence prediction'])
                    table_maker.add_row(['Result',mono_poly,'Prediction whether monoalphabetic or polyalphabetic'])
                    table_maker.add_row(['Key length',key_len,'Key length prediction for TheVigenereSquare cipher only'])
                    print table_maker
            elif cmd_.startswith('SET') or cmd_.startswith('set'):
                try:
                    msg = cmd_.split()[1]
                    cipher = cmd_.split()[2]
                    if msg and msg == 'message' or msg == 'msg':
                        cText = cipher 
                    else:
                        raise IndexError()
                except IndexError:
                    print BERR + " Please specify message [cipher text]" + BEND
                    print "    ex. SET message 'Cipher Text'\n"
            elif cmd_ == 'execute':
                if cText == '':
                    print BERR + "Execution Error.." + BEND
                    print "Please specify message [cipher text]" 
                IC, key_len = Analysis(cText)
                if IC > 0.06:
                    if IC > 0.052:
                        mono_poly = " More likely monoalphabetic"
                        
                    else:
                        mono_poly =  " Probably monoalphabetic" 
                elif IC < 0.045:
                    mono_poly = "{}".format(random.choice([" More likely polyalphabetic"," Probably polyalphabetic"])) 
                print '\n' + BOKMSG + mono_poly + BEND
                print BOKMSG + ' Your Incidence of Coincidence is >>{} {}'.format(BEND,IC)
                print BOKMSG + ' Your key length for TheVigenereSquare cipher is >>{} {}'.format(BEND,key_len)
            elif cmd_ == 'back':
                break
                

