# TASK-01 Implementation of Caesar Cipher
In this task, we have to create a Python program that can encrypt and decrypt text using the Caesar Cipher algorithm. Moreover, it should also allow users to input a message and a shift value to perform encryption and decryption.

# Caesar Cipher
The Caesar Cipher is one of the simplest and most well-known encryption techniques. Named after Julius Caesar, who used it for his private correspondence, it is a type of substitution cipher in which each letter in the plaintext is shifted a certain number of places down or up the alphabet.

**Key Features of the Caesar Cipher**
1. Shift-Based Encryption:
   - Each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.
   - For example, with a shift of 3: A would be replaced by D, B would become E, and so on.

2. Symmetric Encryption:
   - The same shift value is used for both encryption and decryption.
   - To decrypt the message, you shift the letters back by the same number.

3. Alphabet Wrapping:
   - The cipher wraps around the end of the alphabet. For instance, with a shift of 3, X becomes A, Y becomes B, and Z becomes C.

4. Case Insensitivity:
   - Typically, the cipher treats letters as case-insensitive, meaning the same shift is applied regardless of whether a letter is upper or lower case.

5. Preserves Non-Letters:
   - Characters that are not letters (such as numbers, punctuation, and spaces) are typically not altered by the cipher.

**Example**

Plaintext: HELLO
Shift: 3
Encrypted Text: KHOOR

**Encryption and Decryption Algorithm**

Encryption: \( E(x) = (x + n) \mod 26 \)
Decryption: \( D(x) = (x - n) \mod 26 \)
[Here, \( x \) represents the position of the letter in the alphabet (0 for A, 1 for B, ..., 25 for Z), and \( n \) is the shift value.]
