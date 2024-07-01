def caesar_cipher_encrypt(text, shift): #Encryption of Caesar Cipher
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if character is a letter
            shift_amount = shift % 26
            ascii_offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - ascii_offset + shift_amount) % 26 + ascii_offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Non-alphabetical characters
    return encrypted_text

def caesar_cipher_decrypt(text, shift): #Decryption of Caesar Cipher
    return caesar_cipher_encrypt(text, -shift)

def main():
    while True:
        print("\nCaesar Cipher Tools")
        print("Option 1 [Encrypt a message]")
        print("Option 2 [Decrypt a message]")
        print("Option 3 [Exit]")
        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = caesar_cipher_encrypt(message, shift)
            print(f"Encrypted message: {encrypted_message}")

        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_message = caesar_cipher_decrypt(message, shift)
            print(f"Decrypted message: {decrypted_message}")

        elif choice == '3':
            print("Exiting the Caesar Cipher Tool. Goodbye!")
            break

        else:
            print("Invalid choice! Please choose a valid option.")

if __name__ == "__main__":
    main()
