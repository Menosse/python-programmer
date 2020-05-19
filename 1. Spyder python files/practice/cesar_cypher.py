# -*- coding: utf-8 -*-
"""
Created on Mon May 18 17:44:10 2020

@author: Fernando
"""

# sentence = 'the cat sat on the mat'

sentence = '''I confess at these words a shudder passed
through me. There was a thrill in the doctor’s voice
which showed that he was himself deeply moved
by that which he told us. Holmes leaned forward
in his excitement and his eyes had the hard, dry
glitter which shot from them when he was keenly
interested.'''

def cesarCypher(sentence, cypherNum = 5):
    encrypt = ''
    for char in sentence:
        if char == ' ':
            encrypt = encrypt + ' '
        else:
            encrypt = encrypt + (chr(ord(char)+cypherNum))
    return encrypt

def cesarDecypher(sentence, cypherNum = 5):
    decrypt = ''
    for char in sentence:
        if char == ' ':
            decrypt = decrypt + ' '
        else:
            decrypt = decrypt + (chr(ord(char)-cypherNum)) 
    return decrypt

encrypted = cesarCypher(sentence)

decrypted = cesarDecypher(encrypted)

print("Encrypted \n",encrypted,'\n')
print("Decrypted \n", decrypted)