import string

alphabet = string.ascii_lowercase*2

def cipher():
    mod_phrase = ''
    for x in user_input:
        if x == ' ':
            mod_phrase += x
        mod_phrase += alphabet[alphabet.find(x) + (deg % 26)]
    return mod_phrase

deg = int(input('give a degree of rotation...'))
user_input = input("Give me a string: ")

print(cipher())
