# Write a Python Program that translates a message into secret code language.
# Use the rules below to translate normal english into secret code language.

# Coding
# if the word contains at least three characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding
# if the word contains less than three characters,reverse it
# else:
#   remove three characters form start and end, Now remove the last letter and append it to the beginning



import string
import random

def secret_code(word):
    if len(word) >= 3:
        modified = word[1:] + word[0]
        code = "".join(random.choices(string.ascii_letters, k=3))
        code1 = "".join(random.choices(string.ascii_letters, k=3))
        return code + modified + code1
    else:
        return word[::-1]

encode = secret_code("Tarafarugarlaw")
print("Encoded: ",encode)

def decode(word):
    if len(str(word)) >= 3:
        demodify = word[3:-3]
        return demodify[-1] + demodify[:-1]
    else:
        return word[::1]

decoded = decode(encode)
print("Decoded: ",decoded)

        
