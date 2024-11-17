# PRODIGY_CS_01
**Caesar Cipher**

This Python script implements the Caesar cipher, a simple substitution cipher where each letter of the plaintext is shifted a certain number of places down the alphabet.

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

**How to Use:**

1. **Run the Script:**
   Simply run the Python script.

2. **Input:**
   - **Message:** Enter the text you want to encrypt or decrypt.
   - **Shift Value:** Enter the number of positions to shift each letter.

**Example:**

If you input the message "HELLO WORLD" with a shift value of 3, the encrypted message will be "KHOOR ZRUOG". 

**Explanation:**

The `caesar_cipher` function takes the text and shift value as input. It iterates over each character in the text:

1. **Shifting Characters:**
   - If the character is a letter, it shifts its ASCII code by the specified shift value.
   - To ensure the shifted character remains within the alphabet range, a modulo operation is used.
2. **Converting Back to Characters:**
   - The shifted ASCII code is converted back to a character using the `chr()` function.
3. **Handling Non-Alphabetic Characters:**
   - Non-alphabetic characters are added to the result without modification.

## License

This project is open-source and available under the [MIT License](LICENSE).

---

