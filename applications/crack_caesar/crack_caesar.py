# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

import os.path
cipher_txt = os.path.join(os.path.dirname(__file__), 'ciphertext.txt')

with open(cipher_txt) as f:
    cipherText = f.read()

letters = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

