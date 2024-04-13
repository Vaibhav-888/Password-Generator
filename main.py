from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

    # nr_letters = random.randint(8, 10)
    # nr_numbers = random.randint(2, 4)
    # nr_symbols = random.randint(2, 4)

    # Note: these three lines of code of list comprehensions are replaced by the below three for loops
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    #
    # for char in range(nr_numbers):
    #     password_list.append(random.choice(numbers))
    #
    # for char in range(nr_symbols):
    #     password_list.append(random.choice(symbols))

    # PASSWORD = ""
    # for char in range(nr_symbols):
    #     PASSWORD += char

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

"""
1. Create a function called save().
2. Write the data inside the entries to a data.txt file when the add button is clicked.
3. Each website, email and password combination should be on a new line inside the file.
4. All fields need to be cleared after Add button is pressed.
"""


def save():
    website = website_entry.get()
    password = password_entry.get()
    email = email_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Hey! You can't left fields empty.")

    else:
        is_ok = messagebox.askokcancel(title="Credentials save!",
                                       message=f"These are the details entered: \nEmail: {email} "
                                               f"\nPassword: {password} \n Is it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {password} | {email}\n")
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager!")
window.config(pady=50, padx=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entry
website_entry = Entry(width=50)
website_entry.grid(column=1, row=1, columnspan=2)

email_entry = Entry(width=50)
email_entry.insert(0, "vaibhav.lohar87@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

# Buttons

generate_password = Button(text="Generate Password", width=14, command=generate_password)
generate_password.grid(column=2, row=3)

add_button = Button(text="Add", width=42, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
