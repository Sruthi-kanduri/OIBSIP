import random
import string

def generate_password(length, custom_chars):
    if not custom_chars:
        raise ValueError("No characters provided. Please provide at least one character.")
    
    password = ''.join(random.choice(custom_chars) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            raise ValueError("Password length must be greater than zero.")
        
        custom_chars = ""
        
        use_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
        if use_letters:
            letters = input("Enter the specific letters to use: ").strip()
            custom_chars += letters

        use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
        if use_numbers:
            numbers = input("Enter the specific numbers to use: ").strip()
            custom_chars += numbers

        use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'
        if use_symbols:
            symbols = input("Enter the specific symbols to use: ").strip()
            custom_chars += symbols
        
        if not custom_chars:
            raise ValueError("No character types selected. Please select at least one character type or provide custom characters.")
        
        password = generate_password(length, custom_chars)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()