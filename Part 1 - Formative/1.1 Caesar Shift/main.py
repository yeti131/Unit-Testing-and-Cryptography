# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def caesar_encode(text, n):
    caesar_string = ""
    for i in range(len(text)):
        letter = text[i]
        index = alpha.index(letter)
        caesar_string += alpha[(index + n) % 26]
    return caesar_string


def caesar_decode(text, n):
    decode_string = ""
    for i in range(len(text)):
        letter = text[i]
        index = alpha.index(letter)
        decode_string += alpha[(index - n) % 26]
    return decode_string


test = "HELLOWORLD"
shift = 5
enc = caesar_encode(test, shift)
dec = caesar_decode(enc, shift)
print(enc)
print(dec)
# If this worked, dec should be the same as test!
