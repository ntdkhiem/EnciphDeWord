from os import system
from colorama import init
import platform
from core.color import *
from core.banner import banner
from core import Cipher_System

# Global variables
__platform__ = platform.uname()[0]  # System name
__author__ = '@Khiem Nguyen'
ciphers = ['Additive_Cipher', 'Multiplicative_Cipher', 'Affine_Cipher', 'HillDigraph_Cipher', 'HillTrigraph_Cipher','Vigenere_Square']
clear = ''
init() # initalize ANSI color codes for window

if int(platform.python_version_tuple()[0]) < 3:
    f'''{RED} + 'You are using python version {BLUE}{platform.python_version()}{RESET}. Please upgrade to version 3 and run this project again'''
    exit(1)

def main():
    system(clear)
    while 1:
        try:
            banner()
            print(f'''
                {WHITE}1. {CYAN}Additve Cipher{RESET}
                {WHITE}2. {CYAN}Multiplicative Cipher{RESET}
                {WHITE}3. {CYAN}Affine Cipher{RESET}
                {WHITE}4. {CYAN}Hill-Digraph Cipher{RESET}
                {WHITE}5. {CYAN}Hill-Trigraph Cipher{RESET}
                {WHITE}6. {CYAN}Vigenere Square{RESET}
                {WHITE}7. {CYAN}Exit{RESET}
            ''')
            cmd = int(input(f"{RED}Enter {WHITE}(digit only){RESET} >> "))
            if cmd < 7 and cmd > 0:
                second_step(ciphers[cmd - 1])
            elif cmd == 7:
                raise KeyboardInterrupt()
            else:
                raise ValueError()
        except ValueError as e:
            print(f"{RED}[*]{RESET} Please try again!!")
        except KeyboardInterrupt as e:
            print(f"\n\nGOODBYE\n\n")
            exit(1)

def second_step(cipher):
    print (f"{'=' * 10} {WHITE}{cipher}{RESET} {'=' * 10}")
    cipher_Class = Cipher_System(cipher)
    _continue = True
    while _continue:
        print (cipher_Class.get_cipher_info())
        method = input(f'{CYAN}Encrypt{RESET} or {YELLOW}Decrypt{RESET}: ')
        msg = input("Your message: ")
        try: 
            print ('Result >> ', cipher_Class(msg, None, method=method.lower()))
        except ValueError as e:
            print(f'{RED}[*]{RESET} Please follow the instruction!!')
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
        