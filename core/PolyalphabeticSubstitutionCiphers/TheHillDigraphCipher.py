from core.Config import alphabet, C_list

class HillDigraph_Cipher:

    """
        Name: {cyan}The Hill-Digraph Cipher{reset}
        Description: {cyan}An encryption and decryption technique that use 2x2 integer matrices as keys.{reset}
        Possibility: {cyan}456,976{reset}
        Author: {yellow}@Khiem Nguyen{reset}

        [+] There are 4 keys that you need to input!!
        {cyan}HINT{reset}:
            (a = EVEN, b = ODD, c = ODD, d = EVEN)
    """

    def __init__(self, msg, keys):
        self.msg = msg
        if keys == None:
            try:
                self.keys = [int(input('Your key ({}): '.format(name))) for name in ['A','B','C','D']]
            except ValueError as e:
                raise ValueError() 


    def encrypt(self):
        A,B,C,D = self.keys
        enc_list = [self.msg[i:i+2] for i in range(0, len(self.msg), 2)]
        determinant = ((A * D) - (B * C)) % 26
        encrypt_num_list = []
        new_num_list = []
        result = []

        if not determinant in C_list:
            return []
        if len(enc_list[-1]) == 1:
            enc_list.append(enc_list[-1] + 'x')
            enc_list.pop(-2)

        for pair in enc_list:
            encrypt_num_list.append([alphabet.get(char.lower()) for char in pair])
            
        for num_pair in encrypt_num_list:
            first_digit, second_digit = num_pair
            temp_first_letter = ((A * first_digit) + (B * second_digit)) % 26
            temp_second_letter = ((C * first_digit) + (D * second_digit)) % 26
            new_num_list.append([temp_first_letter, temp_second_letter])

        for pair in new_num_list:
            if len(pair) == 1:
                result.append(pair)
            else:
                for number in pair:
                    if number == 0:
                        result.append('Z')
                    else:
                        for letter, index in alphabet.items():
                            if number == index:
                                result.append(letter.upper())

        return ''.join(result)
                
    def decrypt(self):
        A,B,C,D = self.keys
        dec_list = [self.msg[i:i+2] for i in range(0, len(self.msg), 2)]
        determinant = ((A * D) - (B * C)) % 26
        decrypt_num_list = []
        new_num_list = []
        result = []

        if not determinant in C_list:
            return []
        else:
            inverse_determinant = C_list.get(determinant)
            E = ((D  % 26) * inverse_determinant) % 26
            F = (((-1 * B) % 26) * inverse_determinant ) % 26
            G = (((-1 * C) % 26) * inverse_determinant) % 26
            H = ((A % 26) * inverse_determinant) % 26
            
            for two_letters in dec_list:
                decrypt_num_list.append([alphabet.get(letter.lower()) for letter in two_letters])

            for num_pair in decrypt_num_list:
                first_digit, second_digit = num_pair
                temp_first_digit = ((E * first_digit) + (F * second_digit)) % 26
                temp_second_digit = ((G * first_digit) + (H * second_digit)) % 26
                if temp_first_digit == 0:
                    temp_first_digit = 26
                elif temp_second_digit == 0:
                    temp_second_digit = 26
                new_num_list.append([temp_first_digit, temp_second_digit])

            for num_pair in new_num_list:
                for number in num_pair:
                    for letter,index in alphabet.items():
                        if number == index:
                                result.append(letter)
            
            if result[-1] == 'x':
                result.pop()

            return ''.join(result)
