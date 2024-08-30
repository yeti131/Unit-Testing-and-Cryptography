# Project: Vigenere Cipher
It turns out that the Substitution Cipher wasn't a great cipher either; in fact, most newspapers carry a daily puzzle about solving a substitution cipher.  Anything that someone can figure out for fun in an afternoon is not a very secure secret code!

In 1553, a new way of writing secret codes became the new state of the art and stayed that way for centuries.  For about 300 years, there was a secret code called "le chiffre indechiffrable" (the indecipherable cipher) - the Vigenere Cipher.  It wasn't cracked until mathematicians began to study it in the mid-1800s, applying sophisticated statistical analysis tools.

Here's how the Vigenere Cipher works.  First, pick a key word; let's say "TEST".  Then, pick a message you want to encode; let's say "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG".  Imagine writing out the message, and then writing the key word over and over underneath it.  Like this:

```
THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG
TESTTESTTESTTESTTESTTESTTESTTESTTEST
```
To encode the message, go column by column.  Take the two letters in each column and convert them to indices in the alphabet (like Python does, starting with "A" = 0).  Add the two numbers together.  Then, wrapping around if necessary, convert back to a letter.

For example, the first column contains "T" and another "T".  In a zero-indexed alphabet, "T" is index 19.  So, the first colum becomes 19 + 19 = 38.  There are only 26 letters in the alphabet, so imagine counting 0 to 25 and then starting over at the beginning again, where 26 goes back to A.  Counting to 38 ends on M.  (Another way to think about this is that 38 - 26 = 12, and the letter at index 12 is M.)  So, the first column is encoded to the letter M.

The second column is H + E, or 7 + 4, or 11, or L.

In total, the full message encodes this way:

```
THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG
TESTTESTTESTTESTTESTTESTTESTTESTTEST
------------------------------------
MLWJNMUDUVGPGJGQCYEIXHGOXVLAXPSSRHGZ
```
You can read more about the Vigenere Cipher on Wikipedia and many other sites; feel free to Google or search YouTube for other explanations to deepen your knowledge!

---

## Your Task
You should see two function headers in `main.py`.  **Write the two functions so they correctly encode and decode using a given Vigenere Cipher keyword and return the results**.

Some details to consider:
- You might need to spend some time thinking about how to decode a message that's been encoded with a Vigenere Cipher - it's a little tricky!
- You will ONLY get strings made of capital letters.  We won't worry about spaces, lowercase letters, grammar characters, etc.
- You're given `alpha` at the top of your main.py file; use it!
- You should use the above test case to make sure your code is working properly!

Finally, here's a hint - a reminder of how to use a for loop to access each letter in a string by index, instead of looping over each letter directly:

```python
# CORRECT CODE to access by index

for i in range(len(st)):
  print("Index", i, "in string st is", st[i])
```

Notice that the code below **DOES NOT WORK** - this will **not** duplicate the code above.  Can you explain why?

```python
# INCORRECT CODE

for letter in st:
  print("Index", st.index(letter), "in string st is", letter)
```
What goes wrong when you try to use that incorrect code?  Why?  If you're not sure, try running that code with `st = "MISSISSIPPI"`.
  