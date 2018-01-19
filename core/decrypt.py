
import os 
import platform
import random
from prettytable import PrettyTable 
from colortable import table
from core.resources import TheAdditiveCipher
from core.resources import TheMultiplicativeCipher
from core.resources import TheAffineCipher
from utils.color import *
from utils.table_maker import Table_maker,Table_maker_multi
from docs import helper

__platform__ = platform.platform()

def handler():
    while True:
            cmd_decrypt = raw_input("{}{}(Decrypt){} >> ".format(BUNDERLINE,BBLUE,BEND)).strip()
            if cmd_decrypt == 'help' or cmd_decrypt == 'h' or cmd_decrypt == '?':
                help_ = helper.help_('decrypt','out')
                print help_.format(CLIGHTBLUE,CEND)
            elif cmd_decrypt.startswith('show') and cmd_decrypt.endswith('options'):
              if __platform__.startswith('Linux'):
                header = ['ID','Description']
                rows = [['1','The Additive Cipher'],['2','The Multiplicative Cipher']]
                random_color = random.choice(['dark','green','red','blue'])
                print 
                print table(rows,header,colorfmt=random_color)
                print
              else:
                table_maker = PrettyTable()
                table_maker.title = "Information Box"
                table_maker.field_names = ["ID", "Description"]
                table_maker.add_row(["1", "The Additive Cipher"],["2","The Multiplicative Cipher"])
                print table_maker
            elif cmd_decrypt.startswith('use'):
              try: 
                num_given = int(cmd_decrypt.split()[1])
                if num_given == 1:
                  loop_handler('additive',TheAdditiveCipher)
                elif num_given == 2:
                  loop_handler('multiplicative',TheMultiplicativeCipher)
                elif num_given == 3:
                  loop_handler_multi_key('affine',TheAffineCipher)
              except ValueError:
                print BERR + " Please specify ID." + BEND
                print "   ex. SET message 'your string'\n"
                break
              except IndexError:
                print BERR + " Please specify ID." + BEND
                print " ex. use [id]\n"
                break
            elif cmd_decrypt == 'back':
                break
def loop_handler(type,function,keys=False):
    global CORGAN,CEND
    Types = {'additive':'The Additive Cipher','multiplicative':'The Multiplicative Cipher'}
    if keys:
        if keys.isalpha:
            pass
        pass
    else:
        name = [value for key,value in Types.iteritems() if key == type]
        message = ''
        key_num = 0 
        result = ''
        while True:
            comd = raw_input("{0}{1}(Decrypt/{2}{3}{4}){5} >> ".format(BUNDERLINE,BBLUE,CRED,name[0],CEND,BEND)).strip()
            if comd == 'help' or comd == 'h' or comd == '?':
                help_ = helper.help_('decrypt','in')
                print help_.format(CLIGHTBLUE,CEND)
            elif comd.startswith('show') and comd.endswith('info'):
                info_box = Table_maker(message,key_num,result,'decrypt')
                print 
                print info_box
                print 
            elif comd.startswith('SET') or comd.startswith('set'):
                try:
                  msgOrkey = comd.split()[1]
                  strOrnum = comd.rsplit()[2:]
                  if msgOrkey == 'message':
                    message = strOrnum[0]
                    print BOKMSG + " Changing message to >>{} {}\n".format(BEND,message)
                  elif msgOrkey == 'key':
                    key_num = int(strOrnum[0])
                    print BOKMSG + " Changing key to >>{} {}\n".format(BEND,key_num)
                except IndexError:
                  print BERR + " Please specify (message/key) [string/number]" + BEND
                  print "    ex. SET message 'your string'\n"
            elif comd == 'message' or comd == 'msg':
                try:
                  message = raw_input("{}Enter your encrypted string:{} ".format(CGREEN,CEND)).strip()
                  print BOKMSG + " Changing encrypted message to >>{} {}\n".format(BEND,message)
                  for letter in message:
                    if letter.isdigit():
                      raise ValueError()
                    elif message == '':
                      raise ValueError()
                except ValueError:
                  print BERR + " Please don't use digit in your string or none\n" + BEND
            elif comd == 'key':
                try:
                  key_num = int(raw_input("{}How many times you want to encrypt:{} ".format(CGREEN,CEND)).strip())
                  print BOKMSG + " Changing key to >>{} {}\n".format(BEND,key_num)
                except ValueError:
                  print BERR + " Please only use digit as key and not allow spaces\n" + BEND
            elif comd == 'execute':
                try: 
                  if message == '' or key_num == 0:
                    raise ValueError()
                  else:
                    result = function.Decrypt(message,key_num)
                    print "\n" + BOKMSG + ' Your decrypted message is >>{} {}'.format(BEND,result)
                except ValueError:
                  print BERR + " Please set your message/key\n" + BEND
            elif comd == 'back':
                break
def loop_handler_multi_key(type,function):
    Types = {'affine':'The Affine Cipher'}
    name = [value for key,value in Types.iteritems() if key == type]
    message = ''
    result = ''
    keys = [0*i for i in range(9)]
    if type == 'affine':
        for i in range(6):
            keys.pop()
    while True:
        comd = raw_input("{0}{1}(Decrypt/{2}{3}{4}){5} >> ".format(BUNDERLINE,BBLUE,CRED,name[0],CEND,BEND)).strip()
        if comd == 'help' or comd == 'h' or comd == '?':
            help_ = helper.help_('encrypt','in')
            print help_.format(CLIGHTBLUE,CEND)
        elif comd.startswith('show') and comd.endswith('info'):
            info_box = Table_maker_multi(message,keys,result,'decrypt','affine')
            print 
            print info_box
            print 
        elif comd.startswith('SET') or comd.startswith('set'):
            try:
                msgOrkey = comd.split()[1]
                strOrnum = comd.rsplit()[2:]
                if msgOrkey == 'message':
                    message = strOrnum[0]
                    print BOKMSG + " Changing encrypted message to >>{} {}\n".format(BEND,message)
                elif msgOrkey == 'key':
                    keys[0] = int(strOrnum[0])
                    keys[1] = int(strOrnum[1])
                    print BOKMSG + " Changing keyA to >>{} {}\n".format(BEND,keys[0])
                    time.sleep(0.5)
                    print BOKMSG + " Changing keyB to >>{} {}\n".format(BEND,keys[1])
            except IndexError:
                print BERR + " Please specify (message/key(A/B)) [string/number(with space between them)]" + BEND
                print "    ex. SET message 'your string'\n"
                print "    ex. SET key 4 5\n"
        elif comd == 'message' or comd == 'msg':
            try:
              message = raw_input("{}Enter encrypted your string:{} ".format(CGREEN,CEND)).strip()
              print BOKMSG + " Changing encrypted message to >>{} {}\n".format(BEND,message)
              for letter in message:
                if letter.isdigit():
                  raise ValueError()
                elif message == '':
                  raise ValueError()
            except ValueError:
              print BERR + " Please don't use digit in your string or none\n" + BEND
        elif comd == 'key':
            try:
              keys[0] = int(raw_input("{}How many times did you encrypted for keyA:{} ".format(CGREEN,CEND)).strip())
              print BOKMSG + " Changing keyA to >>{} {}\n".format(BEND,keys[0])
              keys[1] = int(raw_input("{}How many times did you encrypted for keyB:{} ".format(CGREEN,CEND)).strip())
              print BOKMSG + " Changing keyB to >>{} {}\n".format(BEND,keys[1])
            except ValueError:
              print BERR + " Please only use digit as key and not allow spaces\n" + BEND
        elif comd == 'execute':
            try: 
              if message == '' or keys[0] == 0:
                raise ValueError()
              else:
                result = function.Decrypt(message,keys)
                if not result:
                    pass
                else:
                    print "\n" + BOKMSG + ' Your encrypted message is >>{} {}'.format(BEND,result)
            except ValueError:
              print BERR + " Please set your message/key\n" + BEND
        elif comd == 'back':
            break











