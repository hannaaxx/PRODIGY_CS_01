def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_char = ord(char) + shift
            if char.isupper():
                shift_char = shift_char % 65 + 65
            else:
                shift_char = shift_char % 97 + 97
            result += chr(shift_char)
        else:
            result += char
    return result

def main():
    text = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))

    encrypted_text = caesar_cipher(text, shift)
    print("Encrypted text:", encrypted_text)

    decrypted_text = caesar_cipher(encrypted_text, -shift)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
