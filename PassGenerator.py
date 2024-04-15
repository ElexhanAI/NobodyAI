import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_passwords():
    passwords = []
    for _ in range(int(entry_password_number.get())):
        PSGeneratorWord = entry_word.get()
        PSGeneratorHowManyNumbers = int(entry_numbers.get())
        PSGeneratorHowManySpecialCharacters = int(entry_special_characters.get())

        Password = PSGeneratorWord 

        for _ in range(PSGeneratorHowManyNumbers):
            Password += random.choice(string.digits)

        for _ in range(PSGeneratorHowManySpecialCharacters):
            Password += random.choice(string.punctuation)

        passwords.append(Password)

    messagebox.showinfo("Generated Passwords", f"Your generated passwords: {', '.join(passwords)}")

    if save_pass.get():
        with open("passwords.txt", "a") as file:
            for password in passwords:
                file.write(password + "\n")
        messagebox.showinfo("Passwords Saved", "Passwords saved successfully.")

root = tk.Tk()
root.title("Password Generator")

label_word = tk.Label(root, text="Enter Your Word:")
label_word.grid(row=0, column=0, padx=10, pady=5)
entry_word = tk.Entry(root)
entry_word.grid(row=0, column=1, padx=10, pady=5)

label_numbers = tk.Label(root, text="How Much Numbers?")
label_numbers.grid(row=1, column=0, padx=10, pady=5)
entry_numbers = tk.Entry(root)
entry_numbers.grid(row=1, column=1, padx=10, pady=5)

label_special_characters = tk.Label(root, text="How Much Special Characters?")
label_special_characters.grid(row=2, column=0, padx=10, pady=5)
entry_special_characters = tk.Entry(root)
entry_special_characters.grid(row=2, column=1, padx=10, pady=5)

label_password_number = tk.Label(root, text="How Many Passwords?")
label_password_number.grid(row=3, column=0, padx=10, pady=5)
entry_password_number = tk.Entry(root)
entry_password_number.grid(row=3, column=1, padx=10, pady=5)

save_pass = tk.BooleanVar()
check_save_pass = tk.Checkbutton(root, text="Save passwords?", variable=save_pass)
check_save_pass.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

button_generate = tk.Button(root, text="Generate Passwords", command=generate_passwords)
button_generate.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
