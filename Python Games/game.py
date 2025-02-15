import random
import time
import tkinter as tk
from tkinter import messagebox

def get_hint(target, guess):
    diff = abs(target - guess)
    if diff == 0:
        return "Correct!"
    elif diff <= 5:
        return "Very Close! 🔥"
    elif diff <= 10:
        return "Close!"
    elif diff <= 20:
        return "Warm!"
    else:
        return "Cold! ❄️"

def start_game(difficulty):
    global target_number, attempts, entry, label_feedback
    
    if difficulty == 'Easy':
        attempts = 15
    elif difficulty == 'Medium':
        attempts = 10
    else:
        attempts = 5
    
    target_number = random.randint(1, 100)
    label_feedback.config(text=f"You have {attempts} attempts. Start guessing!")
    entry.config(state=tk.NORMAL)
    button_submit.config(state=tk.NORMAL)
    entry.delete(0, tk.END)
    print(f"(DEBUG) Target number is: {target_number}")  # Debugging purpose

def check_guess():
    global attempts
    try:
        guess = int(entry.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
        return
    
    if guess < 1 or guess > 100:
        messagebox.showwarning("Out of Range", "Enter a number between 1 and 100.")
        return
    
    hint = get_hint(target_number, guess)
    label_feedback.config(text=hint)
    
    if guess == target_number:
        messagebox.showinfo("Congratulations!", f"You guessed it right in {15 - attempts} attempts!")
        entry.config(state=tk.DISABLED)
        button_submit.config(state=tk.DISABLED)
        return
    
    attempts -= 1
    if attempts == 0:
        messagebox.showinfo("Game Over", f"You're out of attempts! The number was {target_number}.")
        entry.config(state=tk.DISABLED)
        button_submit.config(state=tk.DISABLED)
    else:
        label_attempts.config(text=f"Attempts left: {attempts}")

def reset_game():
    label_feedback.config(text="Select a difficulty to start the game.")
    label_attempts.config(text="")
    entry.config(state=tk.DISABLED)
    button_submit.config(state=tk.DISABLED)

def set_difficulty(diff):
    start_game(diff)

# GUI Setup
import random
target_number = 0
attempts = 0

def set_difficulty(level):
    """Sets difficulty and initializes game settings"""
    global target_number, attempts
    if level == "Easy":
        attempts = 10
        target_number = random.randint(1, 50)
    elif level == "Medium":
        attempts = 7
        target_number = random.randint(1, 100)
    else:
        attempts = 5
        target_number = random.randint(1, 200)

    label_feedback.config(text=f"Difficulty: {level} - Guess a number!")
    label_attempts.config(text=f"Attempts Left: {attempts}")
    entry.config(state=tk.NORMAL)
    button_submit.config(state=tk.NORMAL)

def check_guess():
    """Checks the player's guess and provides feedback"""
    global attempts
    try:
        guess = int(entry.get())
        if guess < target_number:
            feedback = "Too low! Try again."
        elif guess > target_number:
            feedback = "Too high! Try again."
        else:
            feedback = "🎉 Congratulations! You guessed it!"
            entry.config(state=tk.DISABLED)
            button_submit.config(state=tk.DISABLED)

        attempts -= 1
        label_feedback.config(text=feedback)
        label_attempts.config(text=f"Attempts Left: {attempts}")

        if attempts == 0 and guess != target_number:
            label_feedback.config(text=f"Game Over! The number was {target_number}.")
            entry.config(state=tk.DISABLED)
            button_submit.config(state=tk.DISABLED)

    except ValueError:
        label_feedback.config(text="⚠️ Enter a valid number!")

def reset_game():
    """Resets the game to allow a new round"""
    entry.delete(0, tk.END)
    entry.config(state=tk.DISABLED)
    button_submit.config(state=tk.DISABLED)
    label_feedback.config(text="Select a difficulty to start the game.")
    label_attempts.config(text="")

#  LETS Create GUI window -->
import tkinter as tk
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x300")
label_title = tk.Label(root, text="Guess the Number!", font=("Arial", 16))
label_title.pack(pady=10)

# LETS Feedback label...
label_feedback = tk.Label(root, text="Select a difficulty to start the game.", font=("Arial", 12))
label_feedback.pack(pady=5)
label_attempts = tk.Label(root, text="", font=("Arial", 12))
label_attempts.pack()
entry = tk.Entry(root, font=("Arial", 14), state=tk.DISABLED)
entry.pack(pady=10)

# LETS Submit button --> 
button_submit = tk.Button(root, text="Submit Guess", font=("Arial", 12), command=check_guess, state=tk.DISABLED)
button_submit.pack()

# THIS IS Difficulty buttons --> 
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

button_easy = tk.Button(frame_buttons, text="Easy", font=("Arial", 12), command=lambda: set_difficulty('Easy'))
button_easy.grid(row=0, column=0, padx=5)
button_medium = tk.Button(frame_buttons, text="Medium", font=("Arial", 12), command=lambda: set_difficulty('Medium'))
button_medium.grid(row=0, column=1, padx=5)
button_hard = tk.Button(frame_buttons, text="Hard", font=("Arial", 12), command=lambda: set_difficulty('Hard'))
button_hard.grid(row=0, column=2, padx=5)

# This click will Reset buttons --> 
button_reset = tk.Button(root, text="Reset Game", font=("Arial", 12), command=reset_game)
button_reset.pack(pady=10)

root.mainloop()  #LETS run the porgram .-.--->> 

