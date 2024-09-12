# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha_lower = alpha.lower()


def sub_encode(text, codebet):
    """
    Encodes text via a Substitution Cipher.
    :param text: The text to be encoded.
    :param codebet: The alphabet used to substitute characters. Should be 26 characters.
    :return: Encoded text.
    """
    codebet = codebet.upper()
    codebet_lower = codebet.lower()
    encoded_string = ""
    for i in range(len(text)):
        letter = text[i]
        if letter in alpha:
            index = alpha.index(letter)
            encoded_string += codebet[index]
        elif letter in alpha_lower:
            index = alpha_lower.index(letter)
            encoded_string += codebet_lower[index]
        else:
            encoded_string += letter
    return encoded_string


def sub_decode(text, codebet):
    """
    Decodes text via a Substitution Cipher.
    :param text: The text to be decoded.
    :param codebet: The alphabet used to substitute characters. Should be 26 characters.
    :return: Decoded text.
    """
    codebet = codebet.upper()
    codebet_lower = codebet.lower()
    decoded_string = ""
    for i in range(len(text)):
        letter = text[i]
        if letter in alpha:
            index = codebet.index(letter)
            decoded_string += alpha[index]
        elif letter in alpha_lower:
            index = codebet_lower.index(letter)
            decoded_string += alpha_lower[index]
        else:
            decoded_string += letter
    return decoded_string


test = "HELLOWORLD"
cipher_alphabet = "WJKUXVBMIYDTPLHZGONCRSAEFQ"
enc = sub_encode(test, cipher_alphabet)
dec = sub_decode(enc, cipher_alphabet)
print(enc)
print(dec)
# If this worked, dec should be the same as test!
