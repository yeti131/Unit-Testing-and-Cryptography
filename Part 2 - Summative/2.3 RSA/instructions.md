# Project: RSA Encryption
We've worked our way through historical ciphers.  From the easily breakable Caeasar and Substitution Ciphers, to the much more complex Vigenere Cipher which fell to statistical analysis, to the even more complex Affine Cipher which allowed huge groups of letters to be encoded together, and now we reach the present day!

Affine Ciphers still have a problem you probably haven't thought of, which is that anyone that can ENCODE using your Affine Cipher can also DECODE.  I mean, that seems obvious, right?  Anyone who knows your values of n, a, and b will be able to use them to send you secret messages or decode any secret messages sent the same way.

But: what if it was possible to have a cipher that didn't work that way?  Where you could tell everyone, publicly, how to ENCODE messages, and they could encode messages all day long, but only YOU knew how to DECODE them?

This is called an **asymmetric cipher** and its creation is one of the foundations of the modern internet!  It's known as RSA encryption, and it comes from a simple question.  Caesar shifts used *addition* in a mod to encode and decode.  Affine ciphers used *multiplication* in a mod to encode and decode.  What about exponents?

---

## RSA Encryption

Understanding why RSA works takes a lot of studiny number theory, and we won't get into that here.  But we can understand the basic idea.  Here's how RSA works:

- Pick two really big prime numbers, p and q.  (It turns out that mathematicians have found ways to generate really big primes very quickly!)
- Multiply p * q to get m, our encoding/decoding mod.
- Pick e, an encoding exponent.  Someone using this secret code will convert their message to a single number, x, and compute `x ** e (mod m)` to encrypt the message.
- After we get an encoded number, to decode it, we'll raise what the number we get to the power of a different exponent, d.  To find d, though, we won't use mod m!  This is what makes RSA encryption asymmetric.  Instead, we'll make a new mod, t = (p - 1) * (q - 1).  This is called the **totient** of mod m, a number theory concept you don't need to fully understand.  Just know that the modular inverse of e in mod t turns out to be the exponential inverse of e in mod m.  Crazy!
- Keep p, q, t, and d secret.
- Send m and e to everyone.

If I, the user, get your values of m and e, I can do `x**e (mod m)` and send you messages.  But to decode your message I would need to know d.  And in order to know d, I would need to find t, so I could do mod_inverse of e in mod t.  And in order to find t, I need to know p and q, so I could calculate (p - 1) * (q - 1).

...and that leads us to the crucial number theory fact that underlies RSA encryption: it is **very fast** to find two big primes and multiply them together.  It is **very slow** to take that product and factor it back into the two original primes.

Take a look at this link: [how RSA works with examples](https://doctrina.org/How-RSA-Works-With-Examples.html).  Scroll down to "A Real World Example".  Look how huge the primes in the final example are!  It is crazy but it's true - generating big primes like that takes less than a second.  Factoring m (what this website calls n) into those primes would take **hundreds of years**.

So: you can keep d a secret, and send e to everyone, and anyone can send you a secret message, but no one can read them except you.

Cool huh?

---

## Coding RSA

Once you understand the RSA process, there's only one more important fact to know.

To use exponents in a mod, we WON'T write this:
```
y = (x ** e) % m
```
These numbers get **so big** that Python has a hard time handling them!  Instead, Python has a built in function, `pow`, that can do exponents in mods very quickly.  So, instead of the above line of code, we'd write:
```
y = pow(x, e, m)
```
Once that makes sense, write these functions:
-	`get_d(p, q, e)` should use p and q to find the totient of m (as explained above), and then find the multiplicative inverse of e in that modulus, returning the integer.  Feel free to copy/paste the function you were given in the Affine assignment to do this!
    -	A test case: `get_d(2003, 2503, 17)` should return `2946473`.  (And if you think that number is big, you ain’t seen nothin’ yet...)
-	`rsa_encode(text, m, e)` should encode text by converting the entire text block into a single number (using the function you wrote for the Affine assignment) then raising that number to the e power in mod m.
    -	This runs into problems if the user is trying to encode text that is too long, though, so we do need to add something to check for that.  First convert the text to a number, then assert that number is less than the modulus.  If not, throw an error message that explains the problem to the user.  Then, if that assert statement passes without throwing an error, you can do the exponential calculation.
    - Remember that this does not return text!  Since we’re no longer working in a mod that is a power of 26, we aren’t guaranteed that we can turn the resulting number back into text.  So we’ll just leave it encoded as a number!
- `rsa_decode(num, m, d, size)` should decode num by raising it to the d power mod m, and then should convert the resulting number back into a block of text with length given by size.

`main.py` provides this test case:
```
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
```
When you do this, enc should be `34028226424022141662679340496616735128390579906964150145035108807466384852365`.

---

## Making your own RSA key

Below the test case, you'll see code to generate random primes.

The function given takes an argument "n"; this is the number of bits it takes to store each prime that you generate.  Nowadays, n is usually 512; a decade ago, people used 256.  As computers get faster, we can just keep making bigger primes!

As a side note, we usually use e = 65537.  It's a prime number, so it's going to have a modular inverse in mod t, and it's also easy for computers to use since it's really close to 65536, which is a power of 2.

Anyway - you now have everything you need to generate p and q up to the size that professional applications use!  Generate p and q and save them. Use e = 65537. Then, write code to create m, t, and d.  Send anyone m and e; keep the rest for yourself.  And anyone can send you secret messages that only you can decode!

  