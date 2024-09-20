import math

# Copy and paste any functions you need from the Affine assignment!
def mod_inverse_helper(a, b):
  q, r = a // b, a % b
  if r == 1:
    return (1, -1 * q)
  u, v = mod_inverse_helper(b, r)
  return (v, -1 * q * v + u)


def mod_inverse(a, m):
  assert math.gcd(a, m) == 1, "You're trying to invert " + str(a) + " in mod " + str(m) + " and that doesn't work!"
  return mod_inverse_helper(m, a)[1] % m

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
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

# Also write these:

def rsa_encode(text, m, e):
    """
    Encodes text into RSA.
    :param text: Text to encode
    :param m: The modulus factor of the RSA
    :param e: e used to encode
    :return: Encoded text.
    """
    num = convert_to_num(text)
    assert num < m, "Text is too long."
    return pow(num, e, m)


def rsa_decode(num, m, d, l):
    """
    Decodes RSA.
    :param num: Number to decode
    :param m: The modulus factor of the RSA
    :param d: The exponent used to decode
    :param l: The length of the resultant string
    :return: Decoded text.
    """
    num = pow(num, d, m)
    decoded = convert_to_text(num, l)
    return decoded


def get_d(p, q, e):
    """
    Finds the totient and uses it to find d.
    :param p: Prime number used to find t.
    :param q: Prime number used to find d.
    :param e: e used to encode.
    :return: d
    """
    t = (p - 1) * (q - 1)
    return mod_inverse(e, t)

text = "THEFIVEBOXINGWIZARDSJUMPQUICKLY"
l = len(text)
p = 292361466231755597564095925310764764819
q = 307125506157764866722739041634199200019
e = 65537
m = p * q
d = get_d(p, q, e)
enc = rsa_encode(text, m, e)
dec = rsa_decode(enc, m, d, l)
print(enc)
print(dec)
# If this works, dec should be the same as text!

# Part 2: Generate your own key!

from sympy import nextprime
from random import randint

def make_prime(n):
  lower = 2 ** (n - 1) + 1
  upper = 2 ** n - 1
  temp = randint(lower, upper)
  return nextprime(temp)

