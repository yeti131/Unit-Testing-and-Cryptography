# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha_lower = "abcdefghijklmnopqrstuvwxyz"


def caesar_encode(text, n):
    """
    Encodes text via a Caesar Cipher.
    :param text: The text to be encoded.
    :param n: The amount of characters shifted.
    :return: Encoded text.
    """
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
    """
    Decodes text via a Caesar Cipher.
    :param text: The text to be decoded.
    :param n: The amount of characters shifted.
    :return: Decoded text.
    """
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
