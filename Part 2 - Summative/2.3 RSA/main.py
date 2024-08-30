import math

# Copy and paste any functions you need from the Affine assignment!

# Also write these:
def rsa_encode(text, m, e):
  return 0

def rsa_decode(num, m, d, l):
  return ""

def get_d(p, q, e):
  return pow()

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