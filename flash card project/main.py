from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv(r"E:\Python programing Course\Day 31\flash-card-project-start\data\words_to_learn.csv")

data_dict = data.to_dict(orient="records")

# print(data_dict)
current_card = {}


def next_card():
    global current_card, flip_timer
    # global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    print((current_card["French"]))
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    data_dict.remove(current_card)
    print(len(data_dict))
    data = pandas.DataFrame(data_dict)
    data.to_csv(r"E:\Python programing Course\Day 31\flash-card-project-start\data\words_to_learn.csv")


window = Tk()
window.title("Flash Card Game")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file=r"E:\Python programing Course\Day 31\flash-card-project-start\images\card_front.png")
card_back_img = PhotoImage(file=r"E:\Python programing Course\Day 31\flash-card-project-start\images\card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)

# Hold card text, french word, remove placeholder text was title
card_title = canvas.create_text(400, 150, text=" ", font=("Ariel", 40, "italic"))
# Hold card word, english word, remove placeholder text was word
card_word = canvas.create_text(400, 263, text=" ", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

right_img = PhotoImage(file=r"E:\Python programing Course\Day 31\flash-card-project-start\images\right.png")
right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

wrong_img = PhotoImage(file=r"E:\Python programing Course\Day 31\flash-card-project-start\images\wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)


next_card()


window.mainloop()

