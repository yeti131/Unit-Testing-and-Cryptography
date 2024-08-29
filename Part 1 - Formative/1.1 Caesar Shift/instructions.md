# Caesar Shift
The Caesar Shift is one of the earliest known secret codes.  To encode using a Caesar Shift, you shift each letter in your message to the right a certain number of spaces in the alphabet.  For example, encoding `"HELLO"` with a Caesar Shift of `3` would produce `"KHOOR"`.  

Specifically, take `"H"` - start there and count three more letters in the alphabet, `"I"`, `"J"`, `"K"`.  So `"H"` becomes `"K"`.  Etc.

This gets tricky when you reach the end of the alphabet.  For example, consider encoding `"YES"` with a Caesar Shift of `3`.  Starting at `"Y"`, the next letter is `"Z"`... and that's the end of the alphabet!  So we start over from the beginning, and count `"A"`, then `"B"`.  `"Y"` encoded with a shift of `3` `"B"`.  So, `"YES"` would be encoded as `"BHV"`.

There are many places, including Wikipedia, where you can read more about the Caesar Shift if you're interested!

---

## Your Task
You should see two function headers in `main.py`.  Write them so they correctly encode and decode using a given Caesar shift.

You will ONLY get strings made of capital letters.  We won't worry about spaces, lowercase letters, grammar characters, etc.

You're given `alpha` at the top of your main.py file; use it!

Finally, as one way to test yourself: the test that's provided to you - the string `"HELLOWORLD"` with a shift of `5` - should encode to the string `"MJQQTBTWQI"`.  Note that `"W"` becomes `"B"`!