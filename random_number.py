import random
from tkinter import Button, Canvas, Entry, Label, Tk

HEIGHT = 500
WIDTH = 500
BACKGROUND = "#FFFFCC"

window = Tk()
window.title("Random number game")

label1 = Label(window, text="Hello, Welcome to the game", font=('Impact', 20))
label1.pack()
label2 = Label(window, text="This is a number guessing game", font=('Impact', 20))
label2.pack()

attempt=0
RANDOM_NUMBER = 0

def check_number():
    global RANDOM_NUMBER
    num = entry.get()
    try:
        user_number = int(num)
        RANDOM_NUMBER = random.randint(1, user_number)  
        label3.config(text="Range submitted! Now guess the number.")
    except ValueError:
        label3.config(text="Please enter a valid number for the range.")

def check_random_number():
    global RANDOM_NUMBER,attempt
    user_num = entry2.get()
    try:
        user_num = int(user_num)
        if user_num == RANDOM_NUMBER:
            label3.config(text="You've guessed it right!! Congratulations!")
        else:
            attempt+=1
            label3.config(text="Wrong number!! Try again. Attempt:{}".format(attempt))
    except ValueError:
        label3.config(text="Please enter a valid number for guessing.")

canvas = Canvas(window, bg=BACKGROUND, height=HEIGHT, width=WIDTH)
canvas.pack()

canvas.create_text(200, 90, text="Enter a range:", font=('Palatino', 20), fill="#800000")

entry = Entry(window, font=('Palatino', 20))
canvas.create_window(230, 130, window=entry)

button = Button(window, text="Submit", font=('Palatino', 10), command=check_number)
canvas.create_window(410, 130, window=button)

canvas.create_text(200, 160, text="Enter a number:", font=('Palatino', 20), fill="#800000")

entry2 = Entry(window, font=('Palatino', 20))
canvas.create_window(230, 190, window=entry2)

button1 = Button(window, text="Submit", font=('Palatino', 10), command=check_random_number)
canvas.create_window(410, 190, window=button1)

label3 = Label(window, text="Enter the range", font=('Impact', 20))
label3.pack()

window.mainloop()
