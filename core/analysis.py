def Analysis(cipherText):
    alphabet = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', [0] * 27))
    for letter in cipherText:
        if letter.isalpha():
            alphabet[letter] += 1
    
    for key, value in alphabet.items():
        alphabet[key] = value * (value - 1)

    IC = sum(alphabet.values()) / (len(cipherText) * len(cipherText) - 1)
    key_len = abs(((0.027 * len(cipherText)) / (len(cipherText) - 1) * IC - 0.038 * len(cipherText) + 0.065))
    IC = "%.6f" % IC
    key_len = "%.2f" % key_len
    return float(IC), key_len