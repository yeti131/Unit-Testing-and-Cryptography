# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha_lower = "abcdefghijklmnopqrstuvwxyz"


def caesar_encode(text, n):
    try:
        n = int(n)
    except:
        return text
    caesar_string = ""
    for i in range(len(text)):
        letter = str(text[i])
        if letter in alpha:
            index = alpha.index(letter)
            caesar_string += alpha[(index + n) % 26]
        elif letter in alpha_lower:
            index = alpha_lower.index(letter)
            caesar_string += alpha_lower[(index + n) % 26]
        else:
            caesar_string += letter
    return caesar_string


def caesar_decode(text, n):
    try:
        n = int(n)
    except:
        return text
    decode_string = ""
    for i in range(len(text)):
        letter = str(text[i])
        if letter in alpha:
            index = alpha.index(letter)
            decode_string += alpha[(index - n) % 26]
        elif letter in alpha_lower:
            index = alpha_lower.index(letter)
            decode_string += alpha_lower[(index - n) % 26]
        else:
            decode_string += letter
    return decode_string


test = "HELLOWORLD"
shift = 5
enc = caesar_encode(test, shift)
dec = caesar_decode(enc, shift)
print(enc)
print(dec)
# If this worked, dec should be the same as test!
