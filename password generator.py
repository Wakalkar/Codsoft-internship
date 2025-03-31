import random
import string

def generate_password(length, use_uppercase, use_numbers, use_special):
    # Define character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    numbers = string.digits if use_numbers else ''
    special_characters = string.punctuation if use_special else ''
    
    # Combine all chosen character pools
    all_characters = lowercase + uppercase + numbers + special_characters
    
    # Ensure at least one character from each selected pool is included
    password = []
    if use_uppercase:
        password.append(random.choice(uppercase))
    if use_numbers:
        password.append(random.choice(numbers))
    if use_special:
        password.append(random.choice(special_characters))
    
    # Fill the remaining length with random choices from all characters
    remaining_length = length - len(password)
    if remaining_length > 0:
        password += random.choices(all_characters, k=remaining_length)
    
    # Shuffle the password to make it random
    random.shuffle(password)
    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")
    try:
        # Prompt the user for password length
        length = int(input("Enter the desired password length (minimum 6): "))
        if length < 6:
            print("Password length should be at least 6 characters for security.")
            return
        
        # Prompt the user for complexity options
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        use_special = input("Include special characters? (y/n): ").lower() == 'y'
        
        if not (use_uppercase or use_numbers or use_special):
            print("You need to select at least one additional complexity option.")
            return
        
        # Generate the password
        password = generate_password(length, use_uppercase, use_numbers, use_special)
        print("\nGenerated Password:", password)
    
    except ValueError:
        print("Invalid input! Please enter numbers for the length.")

if __name__ == "__main__":
    main()
