from MonoalphabeticSubstitutionCiphers import *
from PolyalphabeticSubstitutionCiphers import *

class Cipher_System:

    _ciphers = {
        'Additive_Cipher': 'the_additive_cipher',
        'Multiplicative_Cipher': 'the_multiplicate_cipher',
        'Affine_Cipher': 'the_affine_cipher',
        'HillDigraph_Cipher' : 'the_hill_digraph_cipher',
        'HillTrigraph_Cipher': 'the_hill_trigraph_cipher',
        'Vigenere_Square': 'the_vigenere_square'
    }

    def __init__(self, type):
        self._type = type

    def __call__(self, method='encrypt', msg='hello', key=0):
        if method == 'encrypt':
            return(eval(self._type).__call__(msg, key).encrypt())
        return(eval(self._type).__call__(msg, key).decrypt())
    
    def get_ciphers(self):
        return [cipher for cipher in self._ciphers.values()]

    def get_cipher_info(self):
        if self._type:
            return [self._ciphers[self._type], eval(self._type).__doc__]
        return 