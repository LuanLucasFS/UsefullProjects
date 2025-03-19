import random
import phrases
import os

#This code is a simple game that gives an encrypted message and the user has to guess the key to decrypt it.
#The key is a random shuffle of the alphabet, so the user has to guess the correct order of the alphabet to decrypt the message.

def create_key():
    key = []
    for i in range(26):
        key.append(chr(i + 65))
    random.shuffle(key)
    return key

def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            encrypted_text += key[ord(char.upper()) - 65]
        else:
            encrypted_text += char
    return encrypted_text

def show_menu():
    print("\n-== Cryptography Game ==-\n")
    print("Enter 'play' to play the game.")
    print("Enter 'exit' to exit.")
    print("\n")

def prepare_phrase(phrase, mode):
    phrase = phrase.upper()
    new_phrase = ""
    if(mode == "easy"):
        for char in phrase:
            if char.isalpha():
                if(random.randint(0, 2) == 0):
                    new_phrase += char
                else:
                    new_phrase += " "
            else:
                new_phrase += char
    elif(mode == "medium"):
        for char in phrase:
            if char.isalpha():
                if(random.randint(0, 4) == 0):
                    new_phrase += char
                else:
                    new_phrase += " "
            else:
                new_phrase += char
    elif(mode == "hard"):
        for char in phrase:
            if char.isalpha():
                if(random.randint(0, 6) == 0):
                    new_phrase += char
                else:
                    new_phrase += " "
            else:
                new_phrase += char
    return new_phrase

def play_game(mode):
    key = create_key()
    if mode == "easy":
        phrase = random.choice(phrases.easy_phrases)
    elif mode == "medium":
        phrase = random.choice(phrases.medium_phrases)
    elif mode == "hard":
        phrase = random.choice(phrases.hard_phrases)
    encrypted_phrase = encrypt(phrase, key)
    prepared_phrase = prepare_phrase(phrase, mode)
    while(True):    
        print("\n-== Cryptography Game ==-\n")

        for char in prepared_phrase:
            print(char + " ", end="")
        print(".")
        for char in encrypted_phrase:
            if char!=" ":
                print("-"+ " ", end="")
            else:
                print("  ", end="")
        print(".")
        for char in encrypted_phrase:
            print(char + " ", end="")

        guess = input("\nGuess the phrase: ")
        if guess.lower() == phrase.lower():
            os.system('cls||clear')
            print("\nCongratulations! You guessed the phrase.")
            print(f"Decrypted phrase: {phrase}")
            break
        else:
            os.system('cls||clear')
            print(f"\nLast Guess: {guess}")
            print("\nWrong key! Try again.")

def main():
    while True:
        show_menu()
        command = input("Enter a command: ")
        if command == "play":
            mode = input("Enter the difficulty level (easy, medium, hard): ")
            play_game(mode)
        elif command == "exit":
            break
        else:
            print("\nInvalid command. Try again.")

if __name__ == "__main__":
    main()




