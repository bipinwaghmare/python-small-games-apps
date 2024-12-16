from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# from random import choice, randint, shuffle
# If we write this way, so we can remove choice,randint and shuffle from everywhere.

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():

    letters = ['A', 'B', 'C', 'D',  'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z''a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u','v', 'w', 'x', 'y','z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']

    letters_no = random.randint(8, 10)
    numbers_no = random.randint(2, 4)
    symbols_no = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(letters_no)]

    # OR password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    # We can write this way also.

    password_number = [random.choice(numbers) for _ in range(numbers_no)]

    password_symbol = [random.choice(symbols) for _ in range(symbols_no)]

    # We use list comprehension for this method

    # for char in range(letters_no):
    #     random_char = random.choice(letters)
    #     password_list.append(random.choice(letters))

    # for number in range(numbers_no):
    #     random_number = random.choice(numbers)
    #     password_list += random_number
    #
    # for symbol in range(symbols_no):
    #     random_symbol = random.choice(symbols)
    #     password_list += random_symbol

    password_list = password_letters + password_number + password_symbol

    # Converting list to string
    random.shuffle(password_list)

    password = "".join(password_list)
    # By using join() method.

    # password = ""

    # for char in password_list:
    #     password = password + char
    #     # # password += char

# print(f"This is your password : {password}")

    password_input.insert(0, password)
    pyperclip.copy(password)
    # pyperclip is user to copy anything automatically.

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops !!!", message="Please don't leave any fields empty!")

    else:
        # messagebox.showinfo(title="Title", message="Message")
        # This only gives one box i.e OK
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n"
                                 f"Email:{email} \nPassword:{password} \nIs it ok to save ?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                # Using with will close the file after use automatically.
                data_file.write(f"{website} || {email} || {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


website_label = Label(text="Website :")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username :")
email_label.grid(column=0, row=2)

password_label = Label(text="Password :")
password_label.grid(column=0, row=3)

website_input = Entry(width=51)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_input = Entry(width=51)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "example@gmail.com")

password_input = Entry(width=32)
password_input.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(width=44, text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2)









window.mainloop()


