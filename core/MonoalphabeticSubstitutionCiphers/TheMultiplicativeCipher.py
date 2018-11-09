from core.Config import alphabet, C_list

class Multiplicative_Cipher:
    
    """
        Name: The Multiplicative Cipher
        Description: An encryption and decryption that use key (1-11) to multiply each number that represent letter in alphabet.
        Possibility: 11
        Author: @Khiem Nguyen

        [+] Please only use digits as key
        HINT:
            Your key: 999
    """

    def __init__(self, msg, key):
        self.msg = msg 
        if key == None:
            try:
                self.key = int(input('Your key: '))
            except ValueError as e:
                raise ValueError() 

    def encrypt(self) :
        if not self.key in C_list:
            return

        encrypt_num_list = []
        result = []

        for letter in self.msg.lower():
            if not letter.isalpha():
                encrypt_num_list.append(letter)
            else:
                encrypted_number = alphabet.get(letter) * self.key 
                if encrypted_number > 26:
                    encrypted_number %= 26
                if encrypted_number == 0:
                    encrypted_number = 26
                encrypt_num_list.append(encrypted_number)
        
        for number in encrypt_num_list:
            if type(number) != int:
                result.append(number)
            else:
                for letter, index in alphabet.items():
                    if number == index:
                        result.append(letter.upper())
                        
        return ''.join(result)

    def decrypt (self) :
        inverse_key = C_list.get(self.key)
        decrypt_num_list = []
        result = []

        for letter in self.msg.lower():
            if not letter.isalpha():
                decrypt_num_list.append(letter)
            else:
                decrypted_number = alphabet.get(letter) * inverse_key % 26
                if decrypted_number > 26:
                    decrypted_number %= 26
                if decrypted_number == 0:
                    decrypted_number = 26
                decrypt_num_list.append(decrypted_number)

        for number in decrypt_num_list:
            if type(number) != int:
                result.append(number)
            else:
                for letter, index in alphabet.items():
                    if number == index:
                        result.append(letter)
        
        return ''.join(result)