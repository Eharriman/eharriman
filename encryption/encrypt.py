import string
from random import seed
from random import random

letter_string = string.ascii_lowercase
letter_list = list(letter_string)

def index_message(messages):
    letter_string = string.ascii_lowercase
    letter_list = list(letter_string)

    idx_list = []
    for message in messages:
        if message in letter_list:
            idx_list.append(letter_list.index(message))
        else:
            return idx_list
    return idx_list

def encrypt_message(index_list):

    prv_key = []
    crypt_message = []

    for index in index_list:
        ran_num = random()
        crypt_message.append(index + ran_num)
        prv_key.append(ran_num)

    return prv_key, crypt_message

def decrypt_message(messages, keys):

    ret = []
    text = ''

    for message in messages:
        for key in keys:
            eval = message - key
            text = text + letter_list[eval]
    return text



print(index_message('sabrina'))
print(encrypt_message([18, 0, 1, 17, 8, 13, 0]))
print(decrypt_message([18.357695400899264, 0.9407785337208571, 1.5214823375539033, 17.542451797655733, 8.936439093809158, 13.232720329895399, 0.8820541202736857], [0.3576954008992639, 0.9407785337208571, 0.5214823375539034, 0.542451797655733, 0.9364390938091579, 0.23272032989539926, 0.8820541202736857]))

# Idea for the encryption:
#   1. Take string message and convert it to a list of the index of lowercase letters
#   2. Add a random number to each string
#   3. Make a list of these random numbers. This will be the private key.
#

# To decrypt the message
#   1. Subtract each number from the literal
#   2. Convert back to ASCII
