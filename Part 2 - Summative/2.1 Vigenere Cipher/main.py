# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def vig_encode(text, keyword):
    iterations = int((len(text) / len(keyword)) + 1)
    key_string = keyword * iterations
    encoded_string = ""
    for i in range(len(text)):
        letter = text[i]
        text_index = alpha.index(letter)
        key_letter = key_string[i]
        key_index = alpha.index(key_letter)
    return ""


def vig_decode(text, keyword):
    return ""


test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
vig_key = "TEST"
enc = vig_encode(test, vig_key)
dec = vig_decode(enc, vig_key)
print(enc)
print(dec)
# If this worked, dec should be the same as test!