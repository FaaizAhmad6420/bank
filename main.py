from tkinter import *
from tkinter import messagebox
import json


# ---------------------------- UPDATE DATA ------------------------------- #
def update_data(new_data):
    with open("data.json", "w") as data_file:
        json.dump(new_data, data_file, indent=4)


# ---------------------------- ADD CASH ------------------------------- #
def add():
    name = name_entry.get().upper()
    account = account_entry.get()
    cash = int(cash_entry.get())

    if len(name) == 0 or len(account) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    elif len(account) != 10:
        messagebox.showinfo(title="Oops", message="'Account #' should be equal to 10 numbers.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

            if account in data:
                old_cash = int(data[account]['cash'])
                data[account]['cash'] = old_cash + cash
            else:
                data[account] = {
                    "name": name,
                    "cash": cash
                }

            update_data(data)

        except FileNotFoundError:
            new_data = {
                account: {
                    "name": name,
                    "cash": cash,
                }
            }
            update_data(new_data)

        finally:
            account_entry.delete(0, END)
            name_entry.delete(0, END)
            cash_entry.delete(0, END)


# ---------------------------- SUBTRACT CASH ------------------------------- #
def subtract():
    name = name_entry.get().upper()
    account = account_entry.get()
    cash = int(cash_entry.get())

    if len(name) == 0 or len(account) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    elif len(account) != 10:
        messagebox.showinfo(title="Oops", message="'Account #' should be equal to 10 numbers.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

            if account in data:
                old_cash = int(data[account]['cash'])
                data[account]['cash'] = old_cash - cash
            else:
                data[account] = {
                    "name": name,
                    "cash": cash
                }

            update_data(data)

        except FileNotFoundError:
            new_data = {
                account: {
                    "name": name,
                    "cash": cash,
                }
            }
            update_data(new_data)

        finally:
            account_entry.delete(0, END)
            name_entry.delete(0, END)
            cash_entry.delete(0, END)


# ---------------------------- FIND ACCOUNT ------------------------------- #
def search():
    account = account_entry.get()
    if len(account) != 10:
        messagebox.showinfo(title="Oops", message="'Account #' should be equal to 10 numbers.")
    else:
        try:
            with open("data.json") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found.")
        else:
            if account in data:
                name = data[account]["name"]
                cash = data[account]["cash"]
                messagebox.showinfo(title=account, message=f"Name: {name}\ncash: {cash}")
            else:
                messagebox.showinfo(title="Error", message=f"No details for {account} exists.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Bank Manager")
window.config(padx=50, pady=50)

# Center the window on the screen
window.update_idletasks()
width = window.winfo_width()
height = window.winfo_height()
x_offset = (window.winfo_screenwidth() - width) // 2
y_offset = (window.winfo_screenheight() - height) // 2
window.geometry(f"+{x_offset}+{y_offset}")

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="bank.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=0, columnspan=2)

# Labels
account_label = Label(text="Account #:")
account_label.grid(row=1, column=0)
name_label = Label(text="Name:")
name_label.grid(row=3, column=0)
cash_label = Label(text="Cash:")
cash_label.grid(row=4, column=0)

# Entries
account_entry = Entry(width=43)
account_entry.grid(row=1, column=1)
name_entry = Entry(width=43)
name_entry.grid(row=3, column=1, columnspan=2)
cash_entry = Entry(width=43)
cash_entry.grid(row=4, column=1)

# Buttons
search_button = Button(text="Details", width=45, command=search)
search_button.grid(row=2, column=0, columnspan=2)
add_button = Button(text="Deposit", width=45, command=add)
add_button.grid(row=5, column=0, columnspan=2)
withdrawal_button = Button(text="Withdrawal", width=45, command=subtract)
withdrawal_button.grid(row=6, column=0, columnspan=2)

window.mainloop()
