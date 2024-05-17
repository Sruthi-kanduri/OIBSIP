import random
import string

def generate_password(length):
    # Define the character sets to use in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password of the specified length
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

# Ask the user to input the desired length of the password
password_length = int(input("Enter the number of characters for the password: "))

# Generate the password
password = generate_password(password_length)

# Print the generated password
print("Generated Password:",password)