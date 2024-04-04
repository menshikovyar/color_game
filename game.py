import random
import tkinter as tk
from tkinter import messagebox, font as tkFont

colours = ['Red', 'Blue', 'Green', 'Yellow', 'Orange', 'Purple', 'Pink', 'Black', 'White']
score = 0
timeleft = 30

def next_colour():
    global score, timeleft

    if timeleft > 0:
        user_input = e.get().lower()
        correct_color = colours[1].lower()

        if user_input == correct_color:
            score += 1

        e.delete(0, tk.END)
        random.shuffle(colours)
        label.config(fg=str(colours[1]), text=str(colours[0]))
        score_label.config(text="Score: " + str(score))

def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        time_label.config(text="Time left: " + str(timeleft))
        time_label.after(1000, countdown)
    else:
        messagebox.showinfo("Time Over", "Your final score is " + str(score))

def start_game(event=None):
    global timeleft
    if timeleft == 30:
        countdown()
    next_colour()

window = tk.Tk()
window.title("Color Game")
window.geometry("450x300")
window.configure(bg="#f0f0f0")

app_font = tkFont.Font(family='Helvetica', size=12)

instructions = tk.Label(window, text="Type in the color of the words, and not the word text!",
                        font=(app_font), bg="#f0f0f0")
instructions.pack(pady=10)

score_label = tk.Label(window, text="Press enter to start", font=(app_font), bg="#f0f0f0")
score_label.pack()

time_label = tk.Label(window, text="Time left: " + str(timeleft), font=(app_font), bg="#f0f0f0")
time_label.pack()

label = tk.Label(window, font=('Helvetica', 60), bg="#f0f0f0")
label.pack(pady=20)

e = tk.Entry(window, justify='center', width=20, font=(app_font))
e.pack()
e.focus_set()

start_button = tk.Button(window, text="Start", command=start_game, width=20, bg="#a0a0a0", fg="#ffffff")
start_button.pack(pady=20)

window.bind('<Return>', start_game)

window.mainloop()
