from core.Config import alphabet

class Vigenere_Square:

    """
        Name: {cyan}The Vigenere Square{reset}
        Description: {cyan}An encryption and decryption technique that use word or string provided as key and adding it to each number that represent letter in alphabet.{reset}
        Possibility: {cyan}limitless{reset}
        Author: {yellow}@Khiem Nguyen{reset}

        [+] You only need to input characters in the as the key
        {cyan}HINT{reset}:
            Your keyword: dog
    """

    def __init__(self,msg, key):
        self.msg = msg
        if key is None:
            try:
                self.keyword = input('Your keyword: ')
            except ValueError as e:
                raise ValueError()

    def encrypt(self):
        key_list = self.keyword * len(self.msg)
        encrypt_num = [alphabet.get(letter) for letter in self.msg]
        encrypt_key = [alphabet.get(key_num) for key_num in key_list]
        new_num = []
        result = []
        
        for i in range(len(encrypt_num)):
            new_num.append((encrypt_num[i] + encrypt_key[i] - 1) % 26)

        for number in new_num:
            if number == 0:
                result.append('Z')
            else:
                for letter,index in alphabet.items():
                    if number == index:
                        result.append(letter.upper())

        return ''.join(result)

    def decrypt(self):
        key_list = self.keyword * len(self.msg)
        decrypt_num = [alphabet.get(letter.lower()) for letter in self.msg]
        decrypt_key = [alphabet.get(key_num.lower()) for key_num in key_list]
        new_num = []
        result = []
        
        for i in range(len(decrypt_num)):
            new_num.append((decrypt_num[i] - decrypt_key[i] + 1) % 26)

        for number in new_num:
            if number == 0:
                result.append('Z')
            else:
                for letter,index in alphabet.items():
                    if number == index:
                        result.append(letter)

        return ''.join(result)