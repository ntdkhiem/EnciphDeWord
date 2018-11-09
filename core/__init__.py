from core.MonoalphabeticSubstitutionCiphers import *
from core.PolyalphabeticSubstitutionCiphers import *
from core.color import YELLOW, CYAN, RESET

class Cipher_System:

    def __init__(self, type):
        self._type = type

    def __call__(self, msg, key, method='encrypt'):
        if method.startswith('e'):
            return(eval(self._type).__call__(msg, key).encrypt())
        print ("[+] Picking decrypt method...")
        return(eval(self._type).__call__(msg, key).decrypt())
    
    def get_cipher_info(self):
        if self._type:
            return eval(self._type).__doc__.format(cyan=CYAN, yellow=YELLOW, reset=RESET)
        return 