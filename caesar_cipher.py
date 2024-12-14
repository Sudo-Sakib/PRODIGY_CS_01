import string

def caesar_cipher(text, shift, mode='encrypt'):
    
    if mode == 'decrypt':
        shift = -shift

    result = []
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - start + shift) % 26 + start
            result.append(chr(shifted))
        else:
            result.append(char)
    return ''.join(result)

def get_valid_integer(prompt):
    """Prompt the user for a valid integer input."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    print("\nWelcome to the Advanced Caesar Cipher Program!")
    print("This tool allows you to encrypt and decrypt messages securely.")

    while True:
        print("\nMain Menu:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ").strip()
        
        if choice == '3':
            print("\nThank you for using the Caesar Cipher Program. Goodbye!")
            break
        
        if choice not in ['1', '2']:
            print("\nInvalid choice. Please select a valid option.")
            continue

        mode = 'encrypt' if choice == '1' else 'decrypt'
        print(f"\nYou selected to {mode} a message.")
        
        text = input("Enter the text: ").strip()
        shift = get_valid_integer("Enter the shift value (integer): ")

        result = caesar_cipher(text, shift, mode)

        print("\n--- Result ---")
        print(f"Original text: {text}")
        print(f"Shift value: {shift}")
        print(f"{mode.capitalize()}ed text: {result}")
        print("--- End of Result ---\n")

        # Ask if the user wants to perform another operation
        again = input("Would you like to perform another operation? (yes/no): ").strip().lower()
        if again not in ['yes', 'y']:
            print("\nExiting program. Have a great day!")
            break
if __name__ == "__main__":
    main()
