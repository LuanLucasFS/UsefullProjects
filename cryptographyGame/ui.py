import tkinter as tk
from tkinter import messagebox
import random
import phrases

class CryptographyGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Cryptography Game")
        self.key = []
        self.phrase = ""
        self.encrypted_phrase = ""
        self.prepared_phrase = ""
        self.input_fields = []

        tk.Label(root, text="Select Difficulty:").pack()
        self.difficulty = tk.StringVar(value="easy")
        difficulties = ["easy", "medium", "hard", "extreme"]
        for diff in difficulties:
            tk.Radiobutton(root, text=diff.capitalize(), variable=self.difficulty, value=diff).pack()

        self.start_button = tk.Button(root, text="Start Game", command=self.start_game)
        self.start_button.pack()
        
        self.display_label = tk.Label(root, text="", font=("Courier", 12), justify="left")
        self.display_label.pack()
        
        self.input_frame = tk.Frame(root)
        self.input_frame.pack()
        
        self.submit_button = tk.Button(root, text="Submit Guess", command=self.check_guess)
        self.submit_button.pack()

    def create_key(self):
        key = [chr(i + 65) for i in range(26)]
        random.shuffle(key)
        return key
    
    def encrypt(self, text, key):
        encrypted_text = "".join(key[ord(char.upper()) - 65] if char.isalpha() else char for char in text)
        return encrypted_text

    def prepare_phrase(self, phrase, mode):
        difficulty_map = {"easy": 2, "medium": 4, "hard": 6, "extreme": 8}
        threshold = difficulty_map.get(mode, 4)
        return "".join(
            char if not char.isalpha() else (char if random.randint(0, threshold) == 0 else "*")
            for char in phrase
        )
    
    def format_display(self, text):
        chunks = [text[i:i+50] for i in range(0, len(text), 50)]
        formatted_lines = []
        for chunk in chunks:
            line = []
            for char in chunk:
                line.append(char + " " if char != " " else "  ")
            formatted_line = "".join(line).strip()
            formatted_lines.append(formatted_line)
        return "\n".join(formatted_lines)
    
    def start_game(self):
        self.key = self.create_key()
        mode = self.difficulty.get()
        self.phrase = random.choice(getattr(phrases, f"{mode}_phrases"))
        self.encrypted_phrase = self.encrypt(self.phrase, self.key)
        self.prepared_phrase = self.prepare_phrase(self.phrase, mode)
        self.display_label.config(text=self.format_display(self.encrypted_phrase))
        
        for widget in self.input_frame.winfo_children():
            widget.destroy()
        
        self.input_fields = []
        prepared_chunks = [self.prepared_phrase[i:i+50] for i in range(0, len(self.prepared_phrase), 50)]
        for chunk in prepared_chunks:
            line_frame = tk.Frame(self.input_frame)
            line_frame.pack(side=tk.TOP, anchor='w')
            for char in chunk:
                if char == "*":
                    entry = tk.Entry(line_frame, width=2, font=("Courier", 12), justify='center')
                    entry.pack(side=tk.LEFT)
                    self.input_fields.append(entry)
                else:
                    # Usar um Label com o caractere (espaço, pontuação ou letra revelada)
                    tk.Label(line_frame, text=char, font=("Courier", 12)).pack(side=tk.LEFT)
    
    def check_guess(self):
        guess = []
        input_index = 0
        for char in self.prepared_phrase:
            if char == "*":
                guess.append(self.input_fields[input_index].get().upper())
                input_index += 1
            else:
                guess.append(char)
        guess_str = "".join(guess)
        
        if guess_str.lower() == self.phrase.lower():
            messagebox.showinfo("Success", f"Congratulations! You guessed the phrase: {self.phrase}")
        else:
            messagebox.showerror("Try Again", "Wrong guess! Keep trying.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CryptographyGame(root)
    root.mainloop()