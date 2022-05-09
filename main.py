import json
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- SEARCH ------------------------------- #
def search():
    website=entry1.get()
    try:
        with open("data.json", 'r') as file:
            data = json.load(file)
            messagebox.showinfo(title=website, message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"No data file found")
    except KeyError:
        messagebox.showinfo(title="Oops", message=f"No details of {website} exist")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list=[choice(letters) for char in range(randint(8, 10))]
    password_list+=[choice(symbols) for char in range(randint(2, 4))]
    password_list+=[choice(numbers) for char in range(randint(2, 4))]
    shuffle(password_list)
    password = "".join(password_list)
    entry3.insert(END,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=entry1.get()
    mail=entry2.get()
    password=entry3.get()
    if website=="" or password=="":
        messagebox.showinfo(title="Oops",message="Please don't leave any field empty.")
        return
    new_data={
        website: {
            "email":mail,
            "password":password,
        }
    }
    is_ok=messagebox.askokcancel(title=website,message=f"Details Entered:\nEmail: {mail}\nPassword: {password}\nIs it okay?")
    if is_ok:
        try:
            with open("data.json", 'r') as file:
                #read old data
                data=json.load(file)
                #update old data with new data
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", 'w') as file:
                json.dump(new_data, file, indent=4)
        except json.decoder.JSONDecodeError:
            with open("data.json", 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("data.json", 'w') as file:
                #save updated data
                json.dump(data,file,indent=4)
        finally:
            entry1.delete(0,"end")
            entry3.delete(0, "end")

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(width=200,height=200,highlightthickness=1)
logo_image=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(row=0,column=1)

label1=Label(text="Website:")
label1.grid(row=1,column=0)

label2=Label(text="Email/Username:")
label2.grid(row=2,column=0)

label3=Label(text="Password:")
label3.grid(row=3,column=0)

entry1=Entry(width=21)
entry1.focus()
entry1.grid(row=1,column=1)

entry2=Entry(width=35)
entry2.insert(END,"vaishnavi@gmail.com")
entry2.grid(row=2,column=1,columnspan=2)

entry3=Entry(width=21)
entry3.grid(row=3,column=1)

button1=Button(text="Search",command=search)
button1.grid(row=1, column=2)

button2=Button(text="Generate Password", command=generate_password)
button2.grid(row=3, column=2)

button3=Button(text="Add", width=36, command=save)
button3.grid(row=4, column=1, columnspan=2)




window.mainloop()