import math

# Read the instructions to see what to do!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# PART 1
# These functions are provided for you!
def mod_inverse_helper(a, b):
    q, r = a//b, a%b
    if r == 1:
        return (1, -1 * q)
    u, v = mod_inverse_helper(b, r)
    return (v, -1 * q * v + u)

def mod_inverse(a, m):
    assert math.gcd(a, m) == 1, "You're trying to invert " + str(a) + " in mod " + str(m) + " and that doesn't work!"
    return mod_inverse_helper(m, a)[1] % m


# These are the functions you'll need to write:
def affine_encode(text, a, b):
    """
    Encodes text via an Affine Cipher.
    :param text: The text to be encoded.
    :param a: Factor used to encode. Must be a modular inverse of b.
    :param b: Factor used to encode. Must be a modular inverse of a.
    :return: Encoded text.
    """
    encoded = ""
    for letter in text:
        index = alpha.index(letter)
        index = index * a % 26
        encoded += alpha[(index + b) % 26]
    return encoded


def affine_decode(text, a, b):
    """
    Decodes text via an Affine Cipher.
    :param text: The text to be decoded.
    :param a: Factor used to encode. Must be a modular inverse of b.
    :param b: Factor used to encode. Must be a modular inverse of a.
    :return: Decoded text.
    """
    decoded = ""
    for letter in text:
        index = alpha.index(letter)
        index = index * b % 26
        decoded += alpha[(index - a) % 26]
    return decoded

test = "HELLOWORLD"
a = 3
b = 9
enc = affine_encode(test, a, b)
dec = affine_decode(enc, a, b)
print(enc)
print(dec)
# If this worked, dec should be the same as test!



# PART 2
# These  are the functions you'll need to write:
def convert_to_num(ngram):
    """
    Converts a ngram into a number.
    :param ngram: ngram to be converted.
    :return: Resultant number.
    """
    num = 0
    count = 0
    for letter in ngram:
        num += 26 ** count * alpha.index(letter)
        count += 1
    return num

def convert_to_text(num, n):
    """
    Converts num into ngram and returns it.
    :param num: Number to convert.
    :param n: Length of ngram to be converted.
    :return: ngram string
    """
    text = ""
    for i in range(n):
        letter_num = num % 26
        text += alpha[letter_num]
        num //= 26

    return text

test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
l = len(test)
num = convert_to_num(test)
answer = convert_to_text(num, l)
print(num)
print(answer)
# If this worked, answer should be the same as test!



# PART 3

# These are the functions you'll need to write:
def affine_n_encode(text, n, a, b):
    while len(text) % n != 0:
        text += "X"
    encoded = ""
    while len(text) != 0:
        letter_set = text[0: 0 + n]
        text = text[n:]
        num = (a * convert_to_num(letter_set) + b) % (26 ** n)
        encoded += convert_to_text(num, n)

    return encoded

def affine_n_decode(text, n, a, b):
    while len(text) % n != 0:
        text += "X"
    decoded = ""
    while len(text) != 0:
        letter_set = text[0: 0 + n]
        text = text[n:]
        num = (b * convert_to_num(letter_set) + a) % (26 ** n)
        decoded += convert_to_text(num, n)

    return decoded

test = "COOL"
n = 3
a = 3
b = 121
enc = affine_n_encode(test, n, a, b)
dec = affine_n_decode(enc, n, a, b)
print(enc, dec)
# If this worked, dec should be the same as test!