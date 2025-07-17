# EnciphDeWord [![Python 3.6.5](https://img.shields.io/badge/Python-3.6.5-yellow.svg)](http://www.python.org/download/)
*Inspired by [Cipher System using SpreadSheet](http://www.mastermathmentor.com/mmm/Crypt.ashx) by @Stu Schawartz*

EnciphDeWord is a Python-based command‑line application designed to help beginners explore and understand classic cryptography.
It provides an interactive environment where users can encrypt and decrypt text using a variety of algorithms—from simple substitution methods to more advanced matrix‑based ciphers. Each algorithm is implemented from scratch in pure Python, allowing users to see exactly how plaintext is transformed into ciphertext and back.

 [![asciicast](https://asciinema.org/a/158352.png)](https://asciinema.org/a/158352?autoplay=1)
 this video is a demo for EnciphDeWord v1

# Requirements
### For this project to work you need :
- [>= Python 3.6](https://www.python.org/downloads/)

### Installation
```
git clone https://github.com/TopKeingt/EnciphDeWord.git
cd EnciphDeWord
python -m pip install -r requirements.txt
python EnciphDeWord.py
```
### TODO:
- [x] Encipher and Decipher
- [X] Include Additive Cipher (26 possibilities :+1:)
- [X] Include Multiplicative Cipher (11 possibilities :+1:)
- [X] Include Affine Cipher (combined of Additive Cipher and Multiplicative Cipher)  (392 possibilities :+1:)
- [X] Include Hill Digraph Cipher (456,976 possibilities :+1:)
- [X] Include Hill Trigraph Cipher (5,429,503,678,976 possibilities :+1:)
- [X] Include Vigenère Square (limitless possibilities :+1:)
- [ ] <del>Include Playfair Cipher</del>
- [ ] <del>Include Permutation Cipher</del>
- [ ] Include exercises for each Cipher
- [X] Include Analysis for encryted message :+1:

### WARNING:
Letters and punctuation work except for digits (I will fix this) so please encrypt your message without adding numbers
