from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
from art import lock_art


# password generator


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    my_new_password = "".join(password_list)
    password_entry.insert(0, my_new_password)
    pyperclip.copy(my_new_password)


def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    data = {
        website:
        {
            'email': email,
            'password': password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message="Please don't leave any field empty!")

    else:
        try:
            with open('data.json', 'r') as data_file:
                new_data = json.load(data_file)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        else:
            new_data.update(data)
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def find_password():
    website = website_entry.get()
    try:
        with open('data.json') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='No Data File Found.')
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f'Email: {email}\nPassword: {password}')
        else:
            messagebox.showinfo(title='Error', message=f'No details for {website} exists.')


window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

# Create a canvas
canvas = Canvas(window, height=200, width=200)
# Display ASCII art on the canvas
text_image = canvas.create_text(100, 100, text=lock_art, font=('Courier', 18))
# Grid placement
canvas.grid(row=0, column=1)


# labels
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)
email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)
password_label = Label(text='Password:')
password_label.grid(row=3, column=0)


# Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'heykashif@gmail.com')
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)


# Buttons
search_button = Button(text='Search', width=10, command=find_password)
search_button.grid(row=1, column=2)
generate_password_button = Button(text='Generate', width=10, command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text='Add', width=10, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
