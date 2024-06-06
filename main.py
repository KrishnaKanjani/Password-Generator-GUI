# ----------------------------------- PASSWORD GENERATOR GUI APP ------------------------------------------- #

from tkinter import *
from tkinter import messagebox
import random
import json

# ------------------------------------ PASSWORD GENERATOR ----------------------------------- #
def password_generator():
    list_of_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    list_of_symbols = ["!","@","#"]
    list_of_numbers = ["1","2","3","4","5","6","7","8","9","0"]

    password_letters = [random.choice(list_of_letters) for _ in range(random.randint(8,10))]
    password_symbols = [random.choice(list_of_symbols) for _ in range(random.randint(1,2))]
    password_numbers = [random.choice(list_of_numbers) for _ in range(random.randint(2,4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)

    password_input.insert(END, string=password)

# ------------------------------------ SAVE DATA -------------------------------------------- #
def save_data():
    website = web_input.get()
    email = mail_input.get()
    password = password_input.get()
    new_data = {
        website : {
            "Email" : email,
            "Password": password
        }
    }
    path = "#Projects\Password-Generator-GUI\saved_passwords.json"

    if len(website)==0 or len(password)==0:
        messagebox.showwarning(title="OPPS!!", message="Some inputs are missing. Please fill them !!")
    else:
        try:
            with open(path, mode="r") as data_file:
                # Reading Old Data
                data = json.load(data_file)
        except json.decoder.JSONDecodeError:
            with open(path, mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating New Data with Old Data
            data.update(new_data)

            with open(path, mode="w") as data_file:
                # Saving Updated Data
                json.dump(data, data_file, indent=4)
        finally:
            web_input.delete(0, END)
            password_input.delete(0, END)


# ------------------------------------------ SEARCH ----------------------------------------- #
def search():
    path = "#Projects\Password-Generator-GUI\saved_passwords.json"
    website = web_input.get()
    try:
        with open(path) as data_file:
            data = json.load(data_file)
    except json.decoder.JSONDecodeError:
        messagebox.showinfo(title="Error", message="The file dosen't exist")
    else:
        if website in data:
            email = data[website]['Email']
            password = data[website]['Password']
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"The details for '{website}' doesn't exists")
        

# -------------------------------------------- UI SETUP -------------------------------------------------- #
window = Tk()
window.title("PASSWORD GENERATOR")
window.config(padx=20, pady=20)
window.resizable(False, False)

canvas = Canvas(height=200, width=200, highlightthickness=0)
photo = PhotoImage(file="#Projects\Password-Generator-GUI\img.png")
canvas.create_image(100,100,image=photo)
canvas.grid(column=1, row=0)

web = Label(text="Website:")
web.grid(column=0, row=1)

web_input = Entry(width=33)
web_input.grid(column=1, row=1)
web_input.focus()

mail = Label(text="Email/Username:")
mail.grid(column=0, row=2)

mail_input = Entry(width=52)
mail_input.grid(column=1, row=2, columnspan=2)
mail_input.insert(0, "krishna@gmail.com")

passw = Label(text="Password:")
passw.grid(column=0, row=3)

password_input = Entry(width=33)
password_input.grid(column=1, row=3)

searchbtn = Button(text="Search", command=search, width=15, bg="lightblue")
searchbtn.grid(column=2, row=1)

generate = Button(text="Generate Password", command=password_generator, bg="lightblue")
generate.grid(column=2, row=3)

add = Button(text="Add", width=44, command=save_data, bg="lightgreen")
add.grid(column=1, row=4, columnspan=2)

window.mainloop()