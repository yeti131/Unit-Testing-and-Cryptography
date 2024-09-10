# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha_lower = alpha.lower()

def vig_encode(text, keyword):
    iterations = int((len(text) / len(keyword)) + 1)
    key_string = (keyword * iterations).upper()
    encoded_string = ""
    for i in range(len(text)):
        letter = text[i]
        if letter in alpha:
            text_index = alpha.index(letter)
            key_letter = key_string[i].upper()
            key_index = alpha.index(key_letter)
            code_index = (text_index + key_index) % 26
            encoded_string += alpha[code_index]
        elif letter in alpha_lower:
            text_index = alpha_lower.index(letter)
            key_letter = key_string[i].upper()
            key_index = alpha.index(key_letter)
            code_index = (text_index + key_index) % 26
            encoded_string += alpha_lower[code_index]
        else:
            encoded_string += letter
            continue

    return encoded_string


def vig_decode(text, keyword):
    iterations = int((len(text) / len(keyword)) + 1)
    key_string = (keyword * iterations).upper()
    decoded_string = ""
    for i in range(len(text)):
        letter = text[i]
        if letter in alpha:
            text_index = alpha.index(letter)
            key_letter = key_string[i].upper()
            key_index = alpha.index(key_letter)
            code_index = (text_index - key_index) % 26
            decoded_string += alpha[code_index]
        elif letter in alpha_lower:
            text_index = alpha_lower.index(letter)
            key_letter = key_string[i].upper()
            key_index = alpha.index(key_letter)
            code_index = (text_index - key_index) % 26
            decoded_string += alpha_lower[code_index]
        else:
            decoded_string += letter
            continue

    return decoded_string


test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
vig_key = "TEST"
enc = vig_encode(test, vig_key)
dec = vig_decode(enc, vig_key)
print(enc)
print(dec)
# If this worked, dec should be the same as test!