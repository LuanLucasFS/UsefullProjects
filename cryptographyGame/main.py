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
    elif(mode == "extreme"):
        for char in phrase:
            if char.isalpha():
                if(random.randint(0, 8) == 0):
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
    elif mode == "extreme":
        phrase = random.choice(phrases.extreme_phrases)
    encrypted_phrase = encrypt(phrase, key)
    prepared_phrase = prepare_phrase(phrase, mode)
    while(True):    
        print("\n-== Cryptography Game ==-\n")
        line1, line2, line3 = "", "", ""
        char_count = 0
        for i in range(len(prepared_phrase)):
            if encrypted_phrase[i] != " ":
                line1 += prepared_phrase[i] + " "
                line2 += "- "
                line3 += encrypted_phrase[i] + " "
                char_count += 1
            else:
                line1 += "  "
                line2 += "  "
                line3 += "  "
            if char_count == 100:  # Quebra a cada 100 caracteres reais (excluindo espaços)
                print(line1 + ".")
                print(line2 + ".")
                print(line3 + "\n")
                line1, line2, line3 = "", "", ""
                char_count = 0

        print(line1)
        print(line2)
        print(line3)
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
            mode = input("Enter the difficulty level (easy, medium, hard, extreme): ")
            play_game(mode)
        elif command == "exit":
            break
        else:
            print("\nInvalid command. Try again.")

if __name__ == "__main__":
    main()




