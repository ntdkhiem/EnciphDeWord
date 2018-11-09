from os import system
import platform
from core.banner import banner
from core import Cipher_System

# Global variables
__platform__ = platform.uname()[0]  # System name
__author__ = '@Khiem Nguyen'
ciphers = ['Additive_Cipher', 'Multiplicative_Cipher', 'Affine_Cipher', 'HillDigraph_Cipher', 'HillTrigraph_Cipher','Vigenere_Square']
clear = ''

if int(platform.python_version_tuple()[0]) < 3:
    print('You are using python version {python_version}. Please upgrade to version 3 and run this project again'.format(platform.python_version))
    exit(1)

def main():
    system(clear)
    while 1:
        try:
            banner()
            print ('''
                1. Additve Cipher
                2. Multiplicative Cipher
                3. Affine Cipher
                4. Hill-Digraph Cipher
                5. Hill-Trigraph Cipher
                6. Vigenere Square
                7. Exit
            ''')
            cmd = int(input("Enter (digit only): "))
            if cmd < 7 and cmd > 0:
                second_step(ciphers[cmd - 1])
            elif cmd == 7:
                raise KeyboardInterrupt()
            else:
                raise ValueError()
        except ValueError as e:
            print("Please try again!!")
        except KeyboardInterrupt as e:
            print("\n\nGOODBYE\n\n")
            exit(1)

def second_step(cipher):
    
    print ("{0}{1}{0}".format("=" * 10, cipher))
    cipher_Class = Cipher_System(cipher)
    _continue = True
    while _continue:
        print (cipher_Class.get_cipher_info())
        method = input('Encrypt or Decrypt: ')
        msg = input("Your message: ")
        try: 
            print ('Result >> ', cipher_Class(msg, None, method=method.lower()))
        except ValueError as e:
            print ('[*] Please follow the instruction!!')
            pass
        _continue = again()

def again():
    if input("Continue? (y/n): ").lower() == 'y':
        return True
    return False

if __name__ == '__main__':
    if 'linux' in __platform__.lower() or 'darwin' in __platform__.lower():
        clear = 'clear'
        system(clear)
        main()
    elif 'window' in __platform__.lower():
        clear = 'cls'
        system(clear)
        main()
    else:
        inp = input("I don't known your operating system but start anyway?(y/n):  ")
        if IDK.lower() == 'y':
            main()
        elif IDK.lower() == 'n':
            exit(0)
        else:
            print ("Please only type 'y' or 'n'!!!")
        