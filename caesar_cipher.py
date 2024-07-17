def caesar_cipher_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():  # Check if character is a letter
            # Shift character within the range of its case (uppercase or lowercase)
            if char.islower():
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif char.isupper():
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            new_char = char  # If character is not a letter, do not encrypt
        ciphertext += new_char
    return ciphertext

def caesar_cipher_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():  # Check if character is a letter
            # Shift character within the range of its case (uppercase or lowercase)
            if char.islower():
                new_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            elif char.isupper():
                new_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            new_char = char  # If character is not a letter, do not decrypt
        plaintext += new_char
    return plaintext

# Main program
def main():
    print("Welcome to the Caesar Cipher encryption/decryption tool!")

    while True:
        choice = input("Enter 'E' for encryption, 'D' for decryption, or 'Q' to quit: ").upper()

        if choice == 'E':
            plaintext = input("Enter the message you want to encrypt: ")
            try:
                shift = int(input("Enter the shift value (a positive integer): "))
                encrypted_message = caesar_cipher_encrypt(plaintext, shift)
                print(f"Encrypted message: {encrypted_message}")
            except ValueError:
                print("Invalid shift value. Please enter a positive integer.")

        elif choice == 'D':
            ciphertext = input("Enter the message you want to decrypt: ")
            try:
                shift = int(input("Enter the shift value used for encryption: "))
                decrypted_message = caesar_cipher_decrypt(ciphertext, shift)
                print(f"Decrypted message: {decrypted_message}")
            except ValueError:
                print("Invalid shift value. Please enter a positive integer.")

        elif choice == 'Q':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter 'E', 'D', or 'Q'.")

if __name__ == "__main__":
    main()