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

# Also write these:

def rsa_encode(text, m, e):
    num = convert_to_num(text)
    assert num < m
    return 0


def rsa_decode(num, m, d, l):
    return ""


def get_d(p, q, e):
    t = (p - 1) * (q - 1)
    return mod_inverse(e, t)

# text = "THEFIVEBOXINGWIZARDSJUMPQUICKLY"
# l = len(text)
# p = 292361466231755597564095925310764764819
# q = 307125506157764866722739041634199200019
# e = 65537
# m = p * q
# d = get_d(p, q, e)
# enc = rsa_encode(text, m, e)
# dec = rsa_decode(enc, m, d, l)
# print(enc)
# print(dec)
# If this works, dec should be the same as text!
print(get_d(2003, 2503, 17))

# Part 2: Generate your own key!

from sympy import nextprime
from random import randint

def make_prime(n):
  lower = 2 ** (n - 1) + 1
  upper = 2 ** n - 1
  temp = randint(lower, upper)
  return nextprime(temp)




'''import math

# Copy and paste any functions you need from the Affine assignment!

# Also write these:
def rsa_encode(text, m, e):
  return 0

def rsa_decode(num, m, d, l):
  return ""

def get_d(p, q, e):
  return 0

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

'''