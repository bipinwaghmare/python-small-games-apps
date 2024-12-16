from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    # timer_text 00:00
    canvas.itemconfig(timer_text, text="00:00")
    # timer_label "Timer"
    timer_label.config(text="Timer")
    # reset check_mark
    check_mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 0:
        # If it's the 2nd, 4th, 6th rep.
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 50, "bold"))

    elif reps % 8 == 0:
        # If it's the 8th rep.
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 50, "bold"))

    else:
        # If it's the 1st, 3rd, 5th, 7th rep.
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):

    count_min = math.floor(count / 60)
    # math.floor prints the largest number less than that whole no. e.g - if 4.8 prints 4.
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
        # Dynamic Typing
    # elif count_sec == 9:
    #     count_sec = "09"
    # elif count_sec == 8:
    #     count_sec = "08"
    # elif count_sec == 7:
    #     count_sec = "07"
    # elif count_sec == 6:
    #     count_sec = "06"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        check_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
# pomodoro = tomato in italian
window.config(padx=100, pady=50, bg=YELLOW, highlightthickness=0)


timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW)
# Canvas is used to overlap things like image,line,rectangle etc.
tomato_img = PhotoImage(file=r"E:\Python programing Course\Day 28\pomodoro-start\tomato.png")
# PhotoImage we use to collect the image we can specify the path also.
canvas.create_image(102, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 32, "bold"))
# In canvas.create_text(*arg, *arg, **kw)
# *arg is positional argument hence x and y position
# **kw kwarg is a keyword argument hence text. string.
canvas.grid(column=1, row=1)


start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label(fg=GREEN, bg=YELLOW, font="bold")
check_mark.grid(column=1, row=3)


window.mainloop()
