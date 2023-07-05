import tkinter as tk
from tkinter import messagebox
from tkinter import *
import threading
from Snake.snake import Game

def run_game(speed):
    game = Game(speed)
    game.play()

window = Tk()
window.geometry("900x600")
image_name = PhotoImage(file="C://Users//11//Desktop//pythonProject//Snake//simg.png")
background_label = Label(window, image=image_name)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

def display_seleted(choice):
    choice = selected_difficulty.get()


selected_difficulty = tk.StringVar()

diff_levels = ["Easy", "Normal", "Hard", "Insane"]
selected_difficulty.set(diff_levels[0])
drop_menu = tk.OptionMenu(window, selected_difficulty, *diff_levels, command=display_seleted)

drop_menu.config(width=12)
drop_menu.config(height=2)

drop_menu.pack(expand=True)

def start_game():
    global speed
    # Check if a difficulty is selected
    if selected_difficulty.get() == "Easy":
        speed = 5
    elif selected_difficulty.get() == "Normal":
        speed = 10
    elif selected_difficulty.get() == "Hard":
        speed = 15
    elif selected_difficulty.get() == "Insane":
        speed = 20

    window.destroy()
    t = threading.Thread(target=run_game, args=(speed,))
    t.start()

def quit_game():
    window.destroy()

start_button = tk.Button(window, text="Start", command=start_game)
start_button.config(width=15, height=3)
start_button.pack()
quit_button = tk.Button(window, text="Quit", command=quit_game)
quit_button.config(width=15, height=3)
quit_button.pack()
window.mainloop()
