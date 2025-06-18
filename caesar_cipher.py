def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char 
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("=== Caesar Cipher Tool ===")
    choice = input("Choose an option: (E)ncrypt or (D)ecrypt: ").strip().upper()

    if choice not in ['E', 'D']:
        print("Invalid choice. Please select 'E' or 'D'.")
        return

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter the shift value: "))
    except ValueError:
        print("Shift must be an integer.")
        return

    if choice == 'E':
        result = encrypt(message, shift)
        print("Encrypted message:", result)
    else:
        result = decrypt(message, shift)
        print("Decrypted message:", result)

if __name__ == "__main__":
    main()
