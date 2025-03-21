import string
import random

# Listing the common character sets
uppercase_letters = string.ascii_uppercase  # A-Z
lowercase_letters = string.ascii_lowercase  # a-z
numbers = string.digits                     # 0-9
special_characters = string.punctuation   # (!@#$%^&*...)

# Creating a list with all accepted characters
all_characters = uppercase_letters + lowercase_letters + numbers + special_characters
all_characters = list(all_characters)

def create_password(length=random.randint(8, 32)):
    """"Generates a secure password with at least one character of each type."""
    if length < 8:
        raise ValueError("Password must be at least 8 characters.")
    
    # Ensures that there is at least one of each type
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Complete with random characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffles to not follow a fixed pattern
    random.shuffle(password)
    return ''.join(password)


def create_key():
    """Generates a random and unique replacement key."""
    key = all_characters.copy()
    random.Random(4).shuffle(key)  # Seed 4 for reproducibility
    return dict(zip(all_characters, key))


def encrypt_password(password, key):
    """Encrypts the password using the provided key"""
    return ''.join(key[char] if char in key else char for char in password)

def decrypt_password(encrypted_password, key):
    """Decrypts the password using the provided key"""
    reverse_key = {v: k for k, v in key.items()}  # Reverse key
    return ''.join(reverse_key[char] if char in reverse_key else char for char in encrypted_password)

def save_password(reason, encrypted_password):
    with open("passwords.txt", "a") as file:
        file.write(f"{reason}: {encrypted_password}\n")

def list_passwords(key):
    try:
        with open("passwords.txt", "r") as file:
            passwords = file.readlines()
        
        for p in passwords:
            reason, encrypted_password = p.strip().split(':', 1)
            decrypted = decrypt_password(encrypted_password.strip(), key)
            print(f"Reason: {reason}, Password: {decrypted}")
    except FileNotFoundError:
        print("No passwords found.")


def remove_password(reason):
    with open("passwords.txt", "r") as file:
        passwords = file.readlines()
    
    with open("passwords.txt", "w") as file:
        for p in passwords:
            stored_reason, _ = p.strip().split(':', 1)
            if stored_reason.strip() != reason.strip():
                file.write(p)


def clear_passwords():
    with open("passwords.txt", "w") as file:
        file.write("")

def main():
    print("\n-== Safe Password Creator ==-\n")
    print("Enter 'create' to generate a new password.")
    print("Enter 'list' to list all saved passwords.")
    print("Enter 'remove' to remove a saved password.")
    print("Enter 'clear' to remove all saved passwords.")
    print("Enter 'exit' to exit.")
    print("\n")
    global key
    key = create_key()

    while True:
        command = input("Enter a command: ")
        if command == "create":
            password = create_password()
            encrypted = encrypt_password(password, key)
            reason = input("Enter a reason for this password: ")
            print(f"Reason: {reason} Password: {password}")
            save_password(reason, encrypted)
        elif command == "list":
            list_passwords(key)
        elif command == "remove":
            reason = input("Enter the reason for the password you want to remove: ")
            remove_password(reason)
        elif command == "clear":
            clear_passwords()
        elif command == "exit":
            break

if __name__ == "__main__":
    main()