# Substitution Cipher
The Caesar Shift wasn't a great secret code; for one thing, there are only a few different possibilities.  (As many letters as you have in your alphabet.)

We can make a code that is much harder to break by scrambling the alphabet completely instead of just shifting to one side.

Define a substitution cipher by scrambling the entire alphabet.  Say, for example, `"WJKUXVBMIYDTPLHZGONCRSAEFQ"`.

Then, imagine writing it out underneath the normal alphabet, in the normal order, like so:

```
ABCDEFGHIJKLMNOPQRSTUVWXYZ
WJKUXVBMIYDTPLHZGONCRSAEFQ
```

To encode a message, replace each letter in the message with the matching letter in the cipher alphabet.  In this case, `"HELLO"` would be encoded as `"MXTTH"`, since M is directly under H, etc.

---

## Your Task
You should see two function headers in `main.py`.  Write them so they correctly encode and decode using a given substitution cipher alphabet.

You will ONLY get strings made of capital letters.  We won't worry about spaces, lowercase letters, grammar characters, etc.

You're given `alpha` at the top of your main.py file; use it!

Finally, as one way to test yourself: the test that's provided to you - the string `"HELLOWORLD"` with the same code alphabet given above - should encode to the string `"MXTTHAHOTU"`.

  