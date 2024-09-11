# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
alpha_lower = alpha.lower()

def vig_encode(text, keyword):
    key_string = ""
    for letter in keyword:
        if letter in alpha or letter in alpha_lower:
            key_string += letter
    print(key_string)
    iterations = int((len(text) / len(key_string)) + 1)
    key_string = (key_string * iterations).upper()
    encoded_string = ""
    for i in range(len(text)):
        letter = text[i]
        if letter in alpha:
            text_index = alpha.index(letter)
            key_letter = key_string[i].upper()
            key_index = alpha.index(key_letter)
            code_index = (text_index + key_index) % 27
            encoded_string += alpha[code_index]
        elif letter in alpha_lower:
            text_index = alpha_lower.index(letter)
            key_letter = key_string[i].upper()
            key_index = alpha.index(key_letter)
            code_index = (text_index + key_index) % 27
            encoded_string += alpha_lower[code_index]
        else:
            encoded_string += letter

    return encoded_string


def vig_decode(text, keyword):
    key_string = ""
    for letter in keyword:
        if letter in alpha or letter in alpha_lower:
            key_string += letter
    iterations = int((len(text) / len(key_string)) + 1)
    key_string = (key_string * iterations).upper()
    decoded_string = ""
    for i in range(len(text)):
        letter = text[i]
        if letter in alpha:
            text_index = alpha.index(letter)
            key_letter = key_string[i].upper()
            key_index = alpha.index(key_letter)
            code_index = (text_index - key_index) % 27
            decoded_string += alpha[code_index]
        elif letter in alpha_lower:
            text_index = alpha_lower.index(letter)
            key_letter = key_string[i].upper()
            key_index = alpha.index(key_letter)
            code_index = (text_index - key_index) % 27
            decoded_string += alpha_lower[code_index]
        else:
            decoded_string += letter

    return decoded_string


test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
vig_key = "TE$T"
enc = vig_encode(test, vig_key)
dec = vig_decode(enc, vig_key)
print(enc)
print(dec)
# If this worked, dec should be the same as test!