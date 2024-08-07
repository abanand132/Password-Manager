import requests
import json
import os
import installation
import random
import webbrowser
from tkinter import *
from tkinter import messagebox
from plyer import notification
from cryptography.fernet import Fernet
import saving_data
import new_account_page
import search
import themes
import search_page
import extra_func as ef
from database import Db
try:
    import pyperclip
except ModuleNotFoundError:
    if messagebox.askyesno(title="Need to download libraries", message='Software needs to install'
                                ' some libraries to work properly.\n\nPress "Yes" to start download'):
        installation.main("pyperclip")


try:
    from ctypes import windll  # Only exists on Windows.

    myappid = "mycompany.myproduct.subproduct.version"
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except:
    pass

# Creating some json files

# Creating basic_info.json file
try:
    with open("basic_info.json", 'r') as text:
        # data = json.load(text)
        pass

except FileNotFoundError:
    with open("basic_info.json", 'w') as d:
        data4 = {
            "email": "",
            "pin": "",
            "theme": "light",
            "code": ""
        }
        json.dump(data4, d, indent=4)

# creating database object
obj = Db()

window = Tk()
window.config(bg="white", padx=30, pady=20)
window.title("Password Manager - Keep your password safe")
window.state('zoomed')


try:
    with open("basic_info.json", 'r') as text:
        data = json.load(text)
    pin_encrypted_value = data['pin']
    if len(data['email']) == 0:
        notify = Label(text="Please Create your account first by clicking on ' Create Account ' button!", bg='yellow')
        notify.config(font=('arial', 13), foreground='black')
        notify.grid(row=14, column=2)
except:
    messagebox.showwarning(title='Failed', message="Unknown Error Occurred! Contact to Developer")


label_strength = Label(text="", bg="white")
label_strength.grid(row=4, column=4)

#-------------------- Adding data to files------#

def add_data_into_file():
    if len(data['email']) > 0:
        saving_data.add_data_into_file(website, email, password, label_strength)
    else:
        messagebox.showwarning(title="Create Account", message="First create a account!")

# def add_data_into_file_encrypt():
#     if len(data['email']) > 0:
#         saving_data.add_data_into_file_encrypt(website, email, password, label_strength)
#     else:
#         messagebox.showwarning(title="Create Account", message="First create a account!")

# # Checkbutton for encryption (encryption checkbutton just below) ------------
# def hello():
#     if checkEncryption.get() == 1:
#         add_data.config(command=add_data_into_file_encrypt)
#
# checkEncryption = IntVar()
# encryption = Checkbutton(text="Encryption", variable=checkEncryption, borderwidth=2, bg="white",
#                          font=("Arial", 10), command=hello)
# encryption.grid(row=5, column=1)

#------------Password Generator (12 character)------#

nos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lower_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
special = ['@',  '#',  '$',  '&',  '*',  ':',  '?']

def strength(password_data):
    if 0 < len(password_data) <= 6:
        label_strength.config(text="Weak", font=("Arial", 10, 'bold'), borderwidth=3, foreground="white", bg="red")
    if 6 < len(password_data) <= 10:
        label_strength.config(text="Medium", font=("Arial", 10, 'bold'), borderwidth=3, foreground="white", bg="orange")
    if len(password_data) > 10:
        label_strength.config(text="Strong", font=("Arial", 10, 'bold'), borderwidth=3, foreground="white", bg="green")

def generate_pass():
    password.delete(0, END)
    generate.config(text="Change Password", font=('arial', 13))
    random.shuffle(nos)
    random.shuffle(lower_alpha)
    random.shuffle(upper_alpha)
    random.shuffle(special)
    x = ""
    for i in range(3):
        x += random.choice(upper_alpha)
        x += random.choice(nos)
        x += random.choice(special)
        x += random.choice(lower_alpha)
    x = list(x)
    random.shuffle(x)
    x = "".join(x)
    password.insert(END, string=x)  # in this way, we insert text in entry box
    pyperclip.copy(password.get())
    strength(x)

#---------------------- Adding Title at Top -----------#
basedir = os.path.dirname(__file__)

my_image = PhotoImage(file=os.path.join(basedir, 'logo.png'))
image_label = Label(image=my_image, bg='white', cursor="hand2")
image_label.grid(row=0, column=2)
image_label.bind("<Button-1>", lambda e: webbrowser.open_new_tab("https://theabhishek.tech/projects/pass-manager.html"))

#--------- Adding different Entry boxes-------#

website = Entry(width=50, font=('arial', 13), borderwidth=1)
website.config(highlightbackground='black', highlightthickness=1, highlightcolor='red')
website.focus()
website.grid(row=2, column=2)

email = Entry(width=50, font=('arial', 13), borderwidth=1)
email.config(highlightbackground='black', highlightthickness=1, highlightcolor='red')
email.grid(row=3, column=2)

password = Entry(width=50, font=('arial', 13), borderwidth=1)
password.config(highlightbackground='black', highlightthickness=1, highlightcolor='red')
password.grid(row=4, column=2)

#---------- Adding different labels boxes-------#
str1 = "                        "
space_label = Label(text=f"{str1}", bg='white', font=('arial', 20))
space_label.grid(row=0, column=0)

label = Label(bg='white')
label.grid(row=20, column=2)

label_website = Label(text="Website : ", bg="white", font=("arial", 13))
label_website.grid(row=2, column=1)

label_email = Label(text="Email/Username : ", bg="white", font=("arial", 13), pady=10)
label_email.grid(row=3, column=1)

label_password = Label(text="Password : ", bg="white", font=("arial", 13))
label_password.config(padx=20)
label_password.grid(row=4, column=1)



def details():
    messagebox.showinfo(title="Details", message="Clear Button : It helps you to clear all 3 fields in 1 click."
        "\n\nAdd Data : It saves all the entered data.\n\nGenerate Password : It gives you strong 12 characters"
        " password. Each time when you click on this button, the password will change.\n\nWhen user click on Generate Password or Add "
        "data then the password will be copied by itself. Then user can paste it anywhere.\n\nYou'll also see "
        "3 colors after clicking add data, that show your password strength\n\nEnable Encryption : It encrypts "
        "all the data entered by the user. It is more secure.But remember, you have to decrypt your data if you want"
        " to use it on the respective websites/apps.\n\n Search : It gives email and password of website (entered by user)"
        " if it is available in the database. User needs to enter website name at appropriate place ")


#---------- Adding different Buttons -------#

generate = Button(text="Generate Password", font=('arial', 13), command=generate_pass, cursor="hand2")
generate.config(bg='white', activebackground='black', activeforeground='white', borderwidth=2)
generate.grid(row=6, column=4)

label1 = Label(text="", bg='white')  # to create space
label1.grid(row=5, column=2)

add_data = Button(text="Add data", width=10, font=("consolas", 14, 'bold'), command=add_data_into_file)
add_data.config(borderwidth=3, bg='black', foreground='white', cursor="hand2")
add_data.grid(row=6, column=2)

detail = Button(text="Help", font=("Arial", 10), command=details, bg='white', cursor="hand2")
detail.grid(row=0, column=1)

k = 0  # to handle error to pressing decrypt button again and again


def report_issue():
    if messagebox.askyesno(title="Report Error", message="Would you like to report any error ?"):
        webbrowser.open_new_tab(url="https://theabhishek.tech")


def search_option_enabling():
    try:
        if len(data['email']) > 0:  # just to force user to create account first
            search_page.search_window(window, data, my_image)
        else:
            messagebox.showwarning(title="Create Account", message="First create a account!")

    except:
        messagebox.showwarning(title='Failed', message="Unknown Error Occurred! Contact to Developer")

search = Button(text="Search 🔎", bg='white', command=search_option_enabling, font=("Arial", 11))
search.config(activeforeground="white", activebackground='black', cursor="hand2")
search.grid(row=0, column=3)


def clear_options():
    # We can clear the content of Entry widget by defining a method delete(0, END) which aims
    # to clear all the content in the range.
    email.delete(0, END)
    website.delete(0, END)
    password.delete(0, END)
    website.focus()
    label_strength.config(text="", bg='white')

clear = Button(text="❌", font=('Consolas', 10), command=clear_options, cursor="hand2")
clear.config(bg='white', activebackground='black', activeforeground='white', borderwidth=1)
clear.grid(row=2, column=4)

def close_func():
    window.destroy()
    # closing the connection
    obj.close_connection()
close = Button(text="Close", font=('Consolas', 11), command=close_func, cursor="hand2")
close.config(bg='white', activebackground='black', activeforeground='white', borderwidth=1)
close.grid(row=0, column=4)

def account_func():
    if os.getenv('ENCRYPTION_KEY_PASS_MANAGER') is not None:
        new_account_page.create_account_func(window)
    else:
        messagebox.showerror(title="Failed", message="Secret-key is not available as environment variable")

create_new_acc = Button(text="Create Account", font=('arial', 9), command=account_func,
                        bg='white', borderwidth=1, cursor="hand2")
create_new_acc.grid(row=10, column=1)

# When account is created then next time text of create account button will change to Update account
try:
    with open('basic_info.json', 'r') as data:
        data = json.load(data)
    if len(data['email']) > 0:
        create_new_acc.config(text='Update Account')
    else:
        create_new_acc.config(text='Create Account')
except:
    raise Exception

credit = Button(text="Report Error", font=("arial", 9), bg='white', command=report_issue)
credit.config(activebackground='blue', activeforeground='black', borderwidth=1, cursor="hand2")
credit.grid(row=12, column=1)


# displaying total no. of passwords
no_of_data = Label(text=f"Total no. of passwords : {obj.total_count()}", bg="white", font=('arial', '11'), pady=10)
no_of_data.grid(row=12, column=2)

def create_popup():
    ef.create_popup(window)

more_btn = Button(text="More..", font=("arial", 9), bg='white', command=create_popup, cursor="hand2")
more_btn.config(borderwidth=1)
more_btn.grid(row=13, column=0)


# checking for secret-key in environment variables
"""
If user opening the app for the first time then a secret-key will be generated which is used to
encrypt the passwords.
If user set the secret-key in environment variable then check it each time when the app opens."""

if os.getenv('ENCRYPTION_KEY_PASS_MANAGER') is None:
    # generate secret-key
    key = Fernet.generate_key()  # unique for each user
    # write it in the txt file
    with open('secret-key.txt', 'w') as file:
        secret_text = ("Variable name : ENCRYPTION_KEY_PASS_MANAGER\n"
                f"Variable value : {key.decode()}")
        file.write(secret_text)

# checking for updates
local_version = 1.2
ver_label = Label(text=f"Version : {local_version}", font=("arial", 10), bg="white")
ver_label.grid(row=13, column=4)

try:
    content = requests.get(url="https://raw.githubusercontent.com/abanand132/Password-Manager/main/app_info.json")
    content = content.json()

    if local_version != content["version"]:
        message = ("New Update is available. Version 1.2 is ready to download\n\n"
                   "Press YES to proceed or NO to continue")
        notification.notify(title=f"Update Available", message=f"Password Manager [v{content['version']}] available"
                                                               f" to download", timeout=10)
        if messagebox.askyesno(title="Update App", message=f"{message}"):
            webbrowser.open_new_tab(url="https://theabhishek.tech/projects/pass-manager.html")
except requests.exceptions.ConnectionError:
    pass


# Dark/light mode functions
def light_mode_func_home():
    themes.light_mode_func_home(window, image_label, website, email, password, label_website, label_email, label_password,
                search, no_of_data, generate, close, clear, detail, label_strength, label, label1, space_label, credit,
                                       create_new_acc, ver_label, more_btn)
    dark_mode_btn.config(bg='white', foreground='black', command=dark_mode_func_home)
    data['theme'] = 'light'
    with open('basic_info.json', 'w') as d1:
        json.dump(data, d1, indent=4)

def dark_mode_func_home():
    themes.dark_mode_func_home(window, image_label, website, email, password, label_website, label_email, label_password,
                search, no_of_data, generate, close, clear, detail, label_strength, label, label1, space_label, credit,
                                       create_new_acc, ver_label, more_btn)
    dark_mode_btn.config(bg='#1A2421', foreground='white', command=light_mode_func_home)
    data['theme'] = 'dark'
    with open('basic_info.json', 'w') as d2:
        json.dump(data, d2, indent=4)


dark_mode_btn = Button(text="☀/🌙", font=('arial', 18), bg='white', foreground='black', borderwidth=0,
                       command=dark_mode_func_home, cursor="hand2")
dark_mode_btn.grid(row=0, column=5)

# to keep in the desired theme

if data['theme'] == 'light':
    light_mode_func_home()
else:
    dark_mode_func_home()



# Hovering
search.bind("<Enter>", func=lambda e: search.config(background='yellow', foreground='black'))
search.bind("<Leave>", func=lambda e: search.config(background='white', foreground='black'))

add_data.bind("<Enter>", func=lambda e: add_data.config(activeforeground="white"))
add_data.bind("<Leave>", func=lambda e: add_data.config(background='black', foreground='white'))

# dark_mode_btn.bind("<Enter>", func=lambda e: dark_mode_btn.config(background='white', foreground='blue'))
# dark_mode_btn.bind("<Leave>", func=lambda e: dark_mode_btn.config(background='white', foreground='black'))


window.iconbitmap(os.path.join(basedir, "logo-icon.ico"))
window.mainloop()
