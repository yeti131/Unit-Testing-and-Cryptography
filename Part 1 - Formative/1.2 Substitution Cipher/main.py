# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def sub_encode(text, codebet):
    encoded_string = ""
    for i in range(len(text)):
        letter = text[i]
        index = alpha.index(letter)
        encoded_string += codebet[index]
    return encoded_string


def sub_decode(text, codebet):
    decoded_string = ""
    for i in range(len(text)):
        letter = text[i]
        index = codebet.index(letter)
        decoded_string += alpha[index]
    return decoded_string


test = "HELLOWORLD"
cipher_alphabet = "WJKUXVBMIYDTPLHZGONCRSAEFQ"
enc = sub_encode(test, cipher_alphabet)
dec = sub_decode(enc, cipher_alphabet)
print(enc)
print(dec)
# If this worked, dec should be the same as test!
