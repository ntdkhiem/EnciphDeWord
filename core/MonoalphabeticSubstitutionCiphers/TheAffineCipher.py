from core.Config import alphabet

C_list_keys = list(filter(lambda x: x != 13, range(1,26,2)))
C_list_values = [27,9,21,15,3,19,7,23,11,5,17,25]

class Affine_Cipher:

    """
        Name: {cyan}The Affine Cipher{reset}
        Description: {cyan}An encryption and decryption that use a combine additive key and multiplicative key to multiply and adding each number that represent letter in alphabet.{reset}
        Possibility: {cyan}392{reset}
        Author: {yellow}@Khiem Nguyen{reset}

        [+] Please only use digits as key
        {cyan}HINT{reset}:
            Your addition key: 5
            Your multiplication key: 20
    """

    def __init__(self, msg, keys):
        self.msg = msg
        if keys == None:
            try:
                self.keys = [int(input('Your addition key: ')), int(input('Your multiplication key: '))]
                if self.keys[0] > 26 or self.keys[1] > 26:
                    raise ValueError()
            except ValueError as e:
                raise ValueError() 

    def encrypt(self):
        if not self.keys[0] in C_list_keys:
            return # None if the first key isn't in the key list.
        else:
            encrypt_num_list = []
            result = []

            for letter in self.msg.lower():
                if not letter.isalpha():
                    encrypt_num_list.append(letter)
                else:
                    encrypt_num_list.append((self.keys[0] * alphabet.get(letter) + self.keys[1]) % 26)
            for number in encrypt_num_list:
                if type(number) != int:
                    result.append(number)
                elif number == 0:
                    result.append('Z')
                else:
                    for letter, index in alphabet.items():
                        if number == index:
                            result.append(letter.upper())
            
            return ''.join(result)

    def decrypt(self):
        CD_list = dict(zip(C_list_keys,C_list_values))
        decrypt_num_list = []
        result = []
        c = 0
        d = 0

        if self.keys[0] % 26 in CD_list.keys():
            c = CD_list.get(self.keys[0] % 26)
            d = (c * (26 - int( self.keys[1] ))) % 26
            
        
        for letter in self.msg.lower():
            if not letter.isalpha():
                decrypt_num_list.append(letter)
            else:
                decrypted_number = (c * alphabet.get(letter) + d) % 26
                if decrypted_number == 0:
                    decrypt_num_list.append(26)
                else:
                    decrypt_num_list.append(decrypted_number)

        for number in decrypt_num_list:
            if type(number) != int:
                result.append(number)
            else:
                for letter, index in alphabet.items():
                    if number == index:
                        result.append(letter)
        
        return ''.join(result)