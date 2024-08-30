# Project: Affine Cipher
After mathematicians used statistical analysis to break the Vigenere Cipher, they turned to a different branch of mathematics - number theory, specifically modular arithmetic - to produce new ciphers.  The first was called the Affine Cipher.

Modular arithmetic is at first a strange idea, but one that works very well for ciphers.  The idea is that you do your arithmetic computations in a certain modulus - in our case, with 26 letters in the alphabet, we're going to pick modulus 26.  And that modulus changes the way arithmetic works.  Any number bigger than 26 is replaced with its remainder when you divide it by 26.  So, for instance, the number 53 would be replaced by 1 in mod 26, because 53 divided by 26 has a remainder of 1.

Another way to think about it is, if you see any number larger than 26, automatically keep subtracting 26 until you get to a number less than 26.  So, 53 would become 27, which would become 1.

Really, the Caesar Shift that you've already learned is just adding a number in mod 26 (after you convert letters to numbers in the first place).  If you take each letter and convert it to a number, then add the shift (in mod 26), you'll get the new number. So, encoding "W" with a +5 Caesar Shift becomes:
```
W + 5 (mod 26) =
22 + 5 (mod 26) = 
27 (mod 26) =
1 (mod 26) = 
B
```

Maybe you even used Python's modular operator, `%`, in your solution!  Saying `x%26` in Python is the same as asking the value of x mod 26.

In any case, mathematicians' next idea was this: instead of ADDING a number in mod 26, can we MULTIPLY instead?  
We have to get into a little bit of number theory here for a moment.  It turns out that division doesn't really work in modular arithmetic (maybe you can experiment and see why), but multiplication works fine.  So, the question here really is this: is it possible to multiply by a certain number in mod 26 to encode, then multiply by a different number to decode?  If we can't rely on division to reverse multiplication, is it possible for multiplication by a different number to serve the same function?

And the answer is yes!  ...sometimes.  It turns out that if you choose a number that has no factors in common with your modulus, then there's a different number you can use to reverse multiplication by the first number.

Here's an example.  In mod 26, multiplying by 3 and 9 reverse each other.  The specific term is **modular inverse** - we say 3 and 9 are modular inverses, because multiplying by one of them reverses multiplying by the other one.

Why is this true?  Well:
```
3 * 9 (mod 26) =
27 (mod 26) =
1 (mod 26)
```
...and multiplying by 1 doesn't change a number!  So if you multiply by 3 and then by 9, that's the same as multiplying by 27, which is the same as multiplying by 1. (Isn't modular arithmetic strange?)  

So, for instance, let's say we encode the message "HI" by multiplying by 3, as follows:
```
H * 3 (mod 26) =
7 * 3 (mod 26) =
21 (mod 26) =
V

I * 3 (mod 26) =
8 * 3 (mod 26) =
24 (mod 26) =
Y
```
So we'd get "VY".  Now let's decode by multiplying by 9:
```
V * 9 (mod 26) =
21 * 9 (mod 26) =
189 (mod 26) =   (just keep subtracting 26s...)
7 (mod 26) =
H

Y * 9 (mod 26) =
24 * 9 (mod 26) =
216 (mod 26) =
8 (mod 26) =
I
```
...and we get back to where we started!

So: we can encode a letter by multiplication in mod 26, as long as we're multiplying by a number that has a modular inverse in mod 26.  (Which is any number that has no factors in common with 26.)

There aren't that many possibilities, though, so to make things a little more complicated, mathematicians decided to add in a caesar shift on top of the multiplication.  Specifically, an Affine Cipher is defined as two numbers "a" and b", so that:
- a is less than 26 and shares no factors in common with the number 26 (ie, it is not a multiple of 2 or 13)
- b is less than 26

...and you encode each letter by converting that letter to a number `x`, then calculating `a*x+b (mod 26)`, then converting that back to a letter.

Take a moment to verify that `"HELLO"`, with `a = 3` and `b = 9`, is encoded to `"EVQQZ"`.

To decode, then, you'd subtract b and multiply by the number that reverses a (in mod 26).

---

## Part 1: Code a Standard Affine Cipher
There are several functions in main.py; for now, focus on `affine_encode` and `affine_decode`.  You want to write functions that correctly encode and decode a message in an Affine Cipher with values of a and b.

To **decode** an Affine Cipher, you'll need to know what to multiply by to reverse the original multiplication.  This is done with the provided function `mod_inverse`.  You don't have to know how this code works, though you can experiment around with it if you like!  The important thing is that, following the example above, if you call `mod_inverse(3, 26)` it will return `9`, and if you call `mod_inverse(9, 26)`, it will return `3`.

You will ONLY get strings made of capital letters.  We won't worry about spaces, lowercase letters, grammar characters, etc.

You're given `alpha` at the top of your main.py file; use it!

Finally, as one way to test yourself: the test that's provided to you - the string `"HELLOWORLD"` with the same a and b values given above - should encode to the string `"EVQQZXZIQS"`.

---

## Part 2: Convert *n*-Grams Instead of Letters

Ok, but, you might be thinking, why is this interesting?  This is still just a substitution cipher, replacing one letter with another one.  And people can crack those for fun!  Why is this a good idea?

Well, something Affine Ciphers - and really any modular arithmetic-based cipher can do - is scale up.  Instead of a substitution cipher that replaces each letter with one single other letter, we can make one that takes each PAIR of letters and replaces them with a specific PAIR of letters.  Or groups of three letters (called 3-grams), or four, or five...

Imagine trying to write down a substitution cipher for pairs of letters.  There are 26 * 26 = 676 different possible pairs!  You'd need a chart with 676 rows!

OR... you can convert each pair of letters into a single number, and do the same `a*x+b` process, and it isn't much more complicated than a standard Affine cipher!

What we need, in order for this to work, is to agree on a way to turn a group of letters into a single number.  There are actually a LOT of different ways to do this!  We'll do one that's pretty simple for a computer to work with.

Take any string of letters, and imagine separating each letter separately and converting it to a number.  For example, if we want to take "ABCZ" and store it as a single number, we would think this:

```
A   B   C   Z
0   1   2   25
```

Then, multiply each of those numbers by increasing powers of 26.

```
A      B      C      Z
0      1      2      25
26**0  26**1  26**2  26**3
```
(Remember, ** makes an exponent in Python!)

So this string would be represented as:
```
0 * 1 + 1 * 26 + 2 * 676 + 25 * 17576 = 440778
```

To go back the other way, you'll need to know how many letters you need to get.  Then for each letter, take the current value and split it into the quotient and remainder when divided by 26.  The quotient is a letter, and the remainder goes back into the same process.  Look:
```
We need 4 letters, so we'll do this 4 times.

440778 divided by 26
quotient: 16953    remainder: 0 = A

16953 divided by 26
quotient: 652      remainder: 1 = B

652 divided by 26
quotient: 25       remainder: 2 = C

25 divided by 26
quotient: 0        remainder: 25 = Z
```
Put the letters together to get ABCZ.

This works because there are 26 letters in the alphabet, so one single letter can't make it all the way to the number 26.  And two letters can't make it all the way to 26**2.  Etc, etc.

In `main.py` you should see two function headers for `convert_to_num` and `convert_to_text`.  Write them to correctly implement the processes above.

Some test cases:

- CB should return 28
- BC should return 53
- BARK should return 187253
- THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG should return 218741750267309021256255930435388550208768849997977

(and of course all of them should be converted back correctly as well!)

---

# Part 3: Affine Cipher on n-Grams

So, the old affine cipher did this:
- Take one letter
- Convert it to a number, x
- Do `a*x+b (mod 26)`
- Convert that back to a letter
- Repeat

Now that we can turn a bunch of letters (a single n-gram) into a single number, we're going to make a new version that is VERY SIMILAR and goes like this:

- Take one n-gram
- Convert it to a number, x
- Do `a*x + b (mod 26**n)`
- Convert that back to an n-gram
- Repeat

For example, let's use n = 2.  That will put us in mod 676 (26**2 = 676).  Let's pick a = 3 and b = 121.  (Now, a and b just have to be less than 676).  Let's encode the message "COOL".  We'll split this into two 2-grams - "CO" and "OL".

```
Convert "CO":
a * x + b (mod 676) =
3 * CO + 121 (mod 676) =
3 * 366 + 121 (mod 676) =
1219 (mod 676) =
543 =
XU

Convert "OL":
a * x + b (mod 676) =
3 * OL + 121 (mod 676) =
3 * 300 + 121 (mod 676) =
1021 (mod 676) =
345 = 
HN
```

So, `affine_n_encode("COOL", 2, 3, 121)` should return `"XUHN"`.

There is only one remaining complication, which is that your string might not be evenly breakable into n-grams.  For instance, if your string is 21 letters long and you want to use 5-grams, then you'll have a missing letter leftover.  **To fix this, we need to add one additional step to the beginning that keeps adding "X" onto the end of the string until the length is an even multiple of n**.  So, here's how I'd convert "COOL" if n was 3 (using the same a = 3 and b = 121 values from before).  "COOL" would now become two *3-grams*, "COO" and "LXX".  Then:

```
n-gram:     COO     LXX
number:     9830    16157
encoded:    12035   13440
new n-gram: XUR     YWT
```
So `affine_n_encode("COOL", 3, 3, 121)` would return "XURYWT".

Code `affine_n_encode` and `affine_n_decode` to match this process.  Use your `convert_to_num` and `convert_to_text` functions from part 2; don't rewrite them again!

Two notes about the decode function:
- You'll need to find `mod_inverse` using `26**n` now, not `26`.
- This function might return strings with extra "X"s on the end; this is ok.

You can use the previous two test cases to verify your code is working.

