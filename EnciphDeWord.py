#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    import os
    import sys
    import platform
    import bcolors as b
    import time
    from colored import fg, attr
    from docs import helper
    from core import encrypt, decrypt, cipherAnalysis
    from core.resources.Banner.banner import banner_show
    from utils.color import *
except ImportError as e:
    error_msg = e.message.split()[3]
    print "[*] Opps, {} file is missing.".format(error_msg)
    print "[*] Try 'pip install -r requirements.txt'"
    # break
    sys.exit(0)
__platform__ = platform.platform()

def main():
      global encrypt
      banner_show()
      help_ = helper.help_('options','none')
      print help_.format(CGREEN,CEND,CWHITE)
      while True:
        try:
          cmd = int(raw_input("{}Enter{} (digit only)>> ".format(BFAIL  ,BEND)))
          if cmd == 1:
            print BOKMSG + " Switching to encrypt..." + BEND
            time.sleep(0.7)
            encrypt.handler()
          elif cmd == 2:
            print BOKMSG + " Switching to decrypt..." + BEND
            time.sleep(0.7)
            decrypt.handler()
          elif cmd == 3:
            print BOKMSG + " Switching to cipher Analysis..." + BEND
            time.sleep(0.7)
            cipherAnalysis.handler()

          elif cmd == 4:
            help_ = helper.help_('options','none')
            print help_.format(CGREEN,CEND,CWHITE)
          elif cmd == 5:
            help_ = helper.help_('author','none')
            print help_.format(CGREEN,CEND,CRED,CLIGHTBLUE,CUNDERLINE,CWHITE)
          elif cmd == 6:
            banner_show()
          elif cmd == 7:
            print "\n\n" + BOKMSG + " GOOD BYE!!!" + BEND
            break
        except ValueError as e:
            error_command = e.message.split()[7]
            print BERR + " Unknown command >> {}{}{}\n".format(CGREEN,error_command,CEND) + BEND
            print "type {}'3'{} for options".format(CGREEN,CEND)
        except KeyboardInterrupt:
            print "\n\n" + BOKMSG + " GOOD BYE!!!" + BEND
            break


if __name__ == '__main__':
    if __platform__.startswith('Linux') or __platform__.startswith('Darwin'):
        os.system('clear')
        main()
    elif __platform__.startswith('Window'):
        os.system('cls')
        main()
    else:
        IDK = raw_input("I don't known your operating system but start anyway?(y/n):  ")
        if IDK.lower() == 'y':
            main()
        elif IDK.lower() == 'n':
            sys.exit(0)
        else:
            print "Please only type 'y' or 'n'!!!"
