from core.Config import alphabet, C_list


class HillTrigraph_Cipher:

    """
        Name: {cyan}The Hill-Trigraph Cipher{reset}
        Description: {cyan}An encryption and decryption technique that use 3x3 integer matrices as keys.{reset}
        Possibility: {cyan}5,429,503,678,976{reset}
        Author: {yellow}@Khiem Nguyen{reset}

        [+] There are 9 keys that you need to input!!
        {cyan}HINT{reset}:
            (a = ODD ,b = ODD,c = EVEN)    (a = EVEN,b = ODD,c = ODD )
            (d = EVEN,e = ODD,f = EVEN) or (d = EVEN,e = ODD,f = ODD )
            (g = EVEN,h = ODD,i = ODD )    (g = ODD ,h = ODD,i = ODD )
    """

    def __init__(self, msg, keys):
        self.msg = msg
        if keys is None:
            try:
                self.keys = [int(input('Your key ({}): '.format(name))) for name in ['A','B','C','D','E','F','G','H','I']]
            except ValueError as e:
                raise ValueError() 

    def encrypt(self):
        A,B,C,D,E,F,G,H,I = self.keys
        enc_list = [self.msg[i:i+3] for i in range(0, len(self.msg), 3)]
        determinant = ((A * E * I) - (A * F * H) - (D * B * I) + (D * C * H) + (G * B * F) - (G * C * E)) % 26
        encrypt_num_list = []
        new_num_list = []
        result = []

        if determinant not in C_list:
            return []
        
        if len(enc_list[-1]) == 1:
            enc_list.append(enc_list[-1] + 'xx')
            enc_list.pop(-2)
        elif len(enc_list[-1]) == 2:
            enc_list.append(enc_list[-1] + 'x')
            enc_list.pop(-2)

        for pair in enc_list:
            encrypt_num_list.append([alphabet.get(char.lower()) for char in pair])

        for num_pair in encrypt_num_list:
            first_digit, second_digit, third_digit = num_pair
            temp_first_digit = ((A * first_digit) + (B * second_digit) + (C * third_digit)) % 26
            temp_second_digit = ((D * first_digit) + (E * second_digit) + (F * third_digit)) % 26
            temp_third_digit = ((G * first_digit) + (H * second_digit) + (I * third_digit)) % 26
            if temp_first_digit == 0:
                temp_first_digit = 26
            elif temp_second_digit == 0:
                temp_second_digit = 26
            elif temp_third_digit == 0:
                temp_third_digit = 26
            new_num_list.append([temp_first_digit, temp_second_digit, temp_third_digit])

        for pair in new_num_list:
            for number in pair:
                if number == 0:
                    result.append('Z')
                else:
                    for letter, index in alphabet.items():
                        if number == index:
                            result.append(letter.upper())
        
        return ''.join(result)

    def decrypt(self):
        A,B,C,D,E,F,G,H,I = self.keys
        dec_list = [self.msg[i:i+3] for i in range(0, len(self.msg), 3)]
        determinant = ((A * E * I) - (A * F * H) - (D * B * I) + (D * C * H) + (G * B * F) - (G * C * E)) % 26
        decrypt_num_list = []
        new_num_list = []
        result = []
        
        if not determinant in C_list:
            return []
        
        inverse_determinant = C_list.get(determinant)
        new_A = ((((E * I) - (F * H))  % 26) * inverse_determinant) % 26
        new_B = ((((C * H) - (B * I)) % 26) * inverse_determinant ) % 26
        new_C = ((((B * F) - (C * E)) % 26) * inverse_determinant) % 26
        new_D = ((((F * G) - (D * I)) % 26) * inverse_determinant) % 26
        new_E = ((((A * I) - (C * G)) % 26) * inverse_determinant) % 26
        new_F = ((((C * D) - (A * F)) % 26) * inverse_determinant) % 26
        new_G = ((((D * H) - (E * G)) % 26) * inverse_determinant) % 26
        new_H = ((((B * G) - (A * H)) % 26) * inverse_determinant) % 26
        new_I = ((((A * E) - (B * D)) % 26) * inverse_determinant) % 26

        for pair in dec_list:
            decrypt_num_list.append([alphabet.get(letter.lower()) for letter in pair])

        for num_pair in decrypt_num_list:
            first_digit, second_digit, third_digit = num_pair
            temp_first_digit = ((new_A * first_digit) + (new_B * second_digit) + (new_C * third_digit)) % 26
            temp_second_digit = ((new_D * first_digit) + (new_E * second_digit) + (new_F * third_digit)) % 26
            temp_third_digit = ((new_G * first_digit) + (new_H * second_digit) + (new_I * third_digit)) % 26
            if temp_first_digit == 0:
                temp_first_digit = 26
            elif temp_second_digit == 0:
                temp_second_digit = 26
            elif temp_third_digit == 0:
                temp_third_digit = 26
            new_num_list.append([temp_first_digit, temp_second_digit, temp_third_digit])
        
        for num_pair in new_num_list:
            for number in num_pair:
                for letter,index in alphabet.items():
                    if number == index:
                            result.append(letter)
        
        if result[-1] == 'x' and result[-2] == 'x':
            result.pop()
            result.pop()
        elif result[-1] == 'x':
            result.pop()
        
        return ''.join(result)