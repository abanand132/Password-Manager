import decrypt_message
import json
import installation
from tkinter import messagebox
try:
    import pyperclip
except ModuleNotFoundError:
    if messagebox.askyesno(title="Need to download libraries", message='Software needs to install'
                                ' some libraries to work properly.\n\nPress "Yes" to start download'):
        installation.main("pyperclip")
import random
import webbrowser
from tkinter import *
from tkinter import messagebox
import saving_data
import change_pin_page
import new_account_page
import search_page
import dark_mode_page

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

# Creating data_files.json file
try:
    with open("data_files.json", 'r') as text1:
        pass
except FileNotFoundError:
        with open("data_files.json", 'w') as d123:
            abc = {
                "e.g.,": {
                    "email": "",
                    "password": "",
                    "status": ""
                }
            }
            json.dump(abc, d123, indent=4)


window = Tk()
window.config(bg="white", padx=20)
window.title("Password Manager - Keep your password safe")
window.state('zoomed')

try:
    with open('data_files.json', 'r') as d:
        data1 = json.load(d)
    no_of_data = Label(text=f"Total no. of passwords : {len(data1.keys())}", bg="white", font=('arial', '11'), pady=10)
    no_of_data.grid(row=12, column=2)

except json.decoder.JSONDecodeError:
    no_of_data = Label(text="Total no. of passwords : 0", bg="white", font=('arial', '11'), pady=10)
    no_of_data.grid(row=12, column=2)

try:
    with open("basic_info.json", 'r') as text:
        data = json.load(text)
    pin_encrypted_value = data['pin']
    if len(data['email']) == 0:
        notify = Label(text="Please Create your account first by clicking on 'Create Account' button!", bg='yellow')
        notify.config(font=('arial', 13), foreground='black')
        notify.grid(row=14, column=2)
except:
    messagebox.showwarning(title='Failed', message="Unknown Error Occurred! Contact to Developer")


nos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lower_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
special = ['@',  '#',  '$',  '&',  '*',  ':',  '?']

label_strength = Label(text="", bg="white")
label_strength.grid(row=5, column=3)

#-------------------- Adding data to files------#

def add_data_into_file():
    try:
        with open("data_files.json", 'r') as dat1:
            dat1 = json.load(dat1)
    except:
        pass
    if website.get().lower() not in dat1.keys():
        if len(data['email']) > 0:
            saving_data.add_data_into_file(website, email, password, label_strength)
        else:
            messagebox.showwarning(title="Create Account", message="First create a account!")
    else:
        messagebox.showwarning(title='Failed', message="Password with same website name is present in the database\n\n"
                                                       "Choose slight different website name to save this data")

def add_data_into_file_encrypt():
    try:
        with open("data_files.json", 'r') as dat1:
            dat1 = json.load(dat1)
    except:
        pass
    if website.get().lower() not in dat1.keys():
        special_list = []
        count = 0
        for i in password.get():
            if not i.isalnum():
                special_list.append(i)
        for i in special_list:
            if i not in special:
                messagebox.showwarning(title="Failed", message=f"Sorry! Only this set of special characters are allowed"
                                                               f" in encryption mode.\n\nSet = {special}")
                count += 1
                break
        if count == 0:
            if len(data['email']) > 0:
                saving_data.add_data_into_file_encrypt(website, email, password, label_strength)
            else:
                messagebox.showwarning(title="Create Account", message="First create a account!")
    else:
        messagebox.showwarning(title='Failed', message="Password with same website name is present in the database\n\n"
                                                       "Choose slight different website name to save this data")

# Checkbutton for encryption (encryption checkbutton just below) ------------
def hello():
    if x.get() == 1:
        add_data.config(command=add_data_into_file_encrypt)

x = IntVar()
encryption = Checkbutton(text="Enable Encryption", variable=x, bg='light yellow', font=("Arial", 13), command=hello)
encryption.grid(row=5, column=1)

#------------Password Generator (12 character)------#
def generate_pass():
    password.delete(0, END)
    generate.config(text=" Change Password ", font=('Consolas', 13))
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

#---------------------- Adding Image at Top -----------#

my_image = PhotoImage(file="pass_manager_image.png")

image_label = Label(image=my_image, bg='white')
image_label.grid(row=0, column=2)
image_label.bind("<Button-1>", lambda e: webbrowser.open_new_tab("https://linktr.ee/abanand132"))

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
label.grid(row=1, column=2)

label_website = Label(text="Website : ", bg="white", font=("arial", 13))
label_website.grid(row=2, column=1)

label_email = Label(text="Email/Username : ", bg="white", font=("arial", 13), pady=10)
label_email.grid(row=3, column=1)

label_password = Label(text="Password : ", bg="white", font=("arial", 13))
label_password.config(padx=20)
label_password.grid(row=4, column=1)



def details():
    messagebox.showinfo(title="Details",message="Clear Button : It helps you to clear all 3 fields in 1 click."
        "\n\nAdd Data : It saves all the entered data.\n\nGenerate Password : It gives you strong 12 characters"
        " password. Each time when you click on this button, the password will change.\n\nWhen user click on Generate Password or Add "
        "data then the password will be copied by itself. Then user can paste it anywhere.\n\nYou'll also see "
        "3 colors after clicking add data, that show your password strength\n\nEnable Encryption : It encrypts "
        "all the data entered by the user. It is more secure.But remember, you have to decrypt your data if you want"
        " to use it on the respective websites/apps.\n\n Search : It gives email and password of website (entered by user)"
        " if it is available in the database. User needs to enter website name at appropriate place ")


#---------- Adding different Buttons -------#

generate = Button(text="Generate Password", font=('arial', 13), command=generate_pass)
generate.config(bg='white', activebackground='black', activeforeground='white', borderwidth=3)
generate.grid(row=4, column=4)

label1 = Label(text="", bg='white')  # to create space
label1.grid(row=5, column=2)

add_data = Button(text="Add data", width=10, font=("consolas", 14, 'bold'), command=add_data_into_file)
add_data.config(activeforeground='black', activebackground="white", borderwidth=3, bg='black', foreground='white')
add_data.grid(row=6, column=2)

detail = Button(text="Details", font=("Arial", 10), command=details, bg='white')
detail.grid(row=0, column=1)

k = 0  # to handle error to pressing decrypt button again and again



def search_option_enabling():
    def search_work():
        pin_value = decrypt_message.decrypt(pin_encrypted_value)
        search_page.search_func(pin_entry, pin_value, website_entry_search, decrypt, window, search_win, delete_data_btn)
    try:
        if len(data['email']) > 0:  # just to force user to create account first

            search_win = Toplevel()
            search_win.title("Search your password")
            search_win.config(bg='white', padx=10, pady=10)
            search_win.state("zoomed")
            window.iconify()

            def change_pin_func():
                change_pin_page.change_pin_func(window, search_win)

            # ---------------------- Adding Image at Top -----------#

            image_label_search_win = Label(search_win, image=my_image, bg='white')
            image_label_search_win.grid(row=0, column=2)
            image_label_search_win.bind("<Button-1>", lambda e: webbrowser.open_new_tab("https://linktr.ee/abanand132"))

            # labels

            space_label1 = Label(search_win, text=f"{str1}", bg='white', font=('arial', 20))
            space_label1.grid(row=0, column=0)

            label_search = Label(search_win, bg='white')
            label_search.grid(row=1, column=2)

            label_search1 = Label(search_win, bg='white')
            label_search1.grid(row=4, column=2)

            label_search2 = Label(search_win, bg='white')
            label_search2.grid(row=5, column=2)

            website_label_search = Label(search_win, text='Website name : ', font=('arial', 13), bg='white')
            website_label_search.grid(row=2, column=1)

            pin_label_search = Label(search_win, text='Enter Pin : ', font=('arial', 13), bg='white', padx=20, pady=10)
            pin_label_search.grid(row=3, column=1)

            # Entries
            website_entry_search = Entry(search_win, width=50, font=('arial', 13), borderwidth=1)
            website_entry_search.config(highlightbackground='black', highlightthickness=1, highlightcolor='red')
            website_entry_search.focus()
            website_entry_search.grid(row=2, column=2)

            pin_entry = Entry(search_win, width=50, font=('arial', 13), borderwidth=1)
            pin_entry.config(highlightbackground='black', highlightthickness=1, highlightcolor='red')
            pin_entry.grid(row=3, column=2)

            # Buttons

            search_btn = Button(search_win, text="Search", width=10, font=("consolas", 15, 'bold'), command=search_work)
            search_btn.config(activeforeground='black', activebackground="white", borderwidth=3, bg='black',
                              foreground='white')
            search_btn.grid(row=6, column=2)

            change_pin_btn = Button(search_win, text="Change PIN?", font=('arial', 10), bg='white',
                                    command=change_pin_func)
            change_pin_btn.grid(row=6, column=1)

            def account_func():
                new_account_page.create_account_func(window)

            create_new_acc_search = Button(search_win, text="Update Account", font=('Consolas', 11),
                                           command=account_func, bg='white')
            create_new_acc_search.grid(row=8, column=1)

            def clear_options_func():
                # We can clear the content of Entry widget by defining a method delete(0, END) which aims
                # to clear all the content in the range.
                search_win.destroy()
                search_option_enabling()

            clear_search = Button(search_win, text="Refresh", font=('Consolas', 11), command=clear_options_func)
            clear_search.config(bg='white', activebackground='black', activeforeground='white', borderwidth=2)
            clear_search.grid(row=6, column=3)

            def close_function():
                search_win.destroy()
                if data['theme'] == 'light':
                    light_mode_func_home()
                else:
                    dark_mode_func_home()
                window.state("zoomed")

            close_search = Button(search_win, text="Back to Home", font=('Consolas', 11), command=close_function)
            close_search.config(bg='white', activebackground='black', activeforeground='white', borderwidth=2)
            close_search.grid(row=0, column=4)

            decrypt = Button(search_win, text="", bg='white', borderwidth=0, font=('arial', 11), foreground='white')
            decrypt.grid(row=2, column=4)

            delete_data_btn = Button(search_win, text="", bg='white', borderwidth=0, font=('arial', 11), foreground='white')
            delete_data_btn.grid(row=3, column=4)

            credit_search = Button(search_win, text="Made by Abhishek (click me)", font=("consolas", 11), bg='white')
            credit_search.bind("<Button-1>", lambda e: webbrowser.open_new_tab("https://linktr.ee/abanand132"))

            credit_search.config(activebackground='blue', activeforeground='black')
            credit_search.grid(row=10, column=2)

            def light_mode_search():
                dark_mode_page.light_mode_func_search(image_label_search_win, search_win, space_label1, label_search,
                   label_search1, label_search2, close_search, clear_search, create_new_acc_search, change_pin_btn,
                   search_btn, pin_entry, pin_label_search, website_label_search, website_entry_search, decrypt,
                                                      delete_data_btn)

                dark_mode_btn_search.config(bg='white', foreground='black', command=dark_mode_search)

                data['theme'] = 'light'
                with open('basic_info.json', 'w') as d1:
                    json.dump(data, d1, indent=4)

            def dark_mode_search():
                dark_mode_page.dark_mode_func_search(image_label_search_win, search_win, space_label1, label_search,
                                                     label_search1, label_search2, close_search,
                                                     clear_search, create_new_acc_search, change_pin_btn, search_btn,
                                                     pin_entry, pin_label_search,
                                                     website_label_search, website_entry_search, decrypt, delete_data_btn)

                dark_mode_btn_search.config(bg='black', foreground='white', command=light_mode_search)

                data['theme'] = 'dark'
                with open('basic_info.json', 'w') as d1:
                    json.dump(data, d1, indent=4)

            dark_mode_btn_search = Button(search_win, text="🌑", font=('arial', 30), bg='white', foreground='black',
                                          borderwidth=0,
                                          command=dark_mode_search)
            dark_mode_btn_search.grid(row=10, column=3)

            if data['theme'] == 'light':
                light_mode_search()
            else:
                dark_mode_search()

            search_win.grab_set()

        else:
            messagebox.showwarning(title="Create Account", message="First create a account!")

    except:
        messagebox.showwarning(title='Failed', message="Unknown Error Occurred! Contact to Developer")

search = Button(text="Search ", bg='white', command=search_option_enabling, font=("Arial", 12))
search.config(activeforeground="white", activebackground='black')
search.grid(row=0, column=3)


def clear_options():
    # We can clear the content of Entry widget by defining a method delete(0, END) which aims
    # to clear all the content in the range.
    email.delete(0, END)
    website.delete(0, END)
    password.delete(0, END)
    website.focus()
    label_strength.config(text="", bg='white')

clear = Button(text="Clear", font=('Consolas', 11), command=clear_options)
clear.config(bg='white', activebackground='black', activeforeground='white', borderwidth=2)
clear.grid(row=6, column=3)

def close_func():
    window.destroy()
close = Button(text="Close", font=('Consolas', 11), command=close_func)
close.config(bg='white', activebackground='black', activeforeground='white', borderwidth=2)
close.grid(row=0, column=4)


def account_func():
    new_account_page.create_account_func(window)

create_new_acc = Button(text="Create Account", font=('Consolas', 11), command=account_func, bg='white')
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
    pass

credit = Button(text="Made by Abhishek (click me)", font=("consolas", 11), bg='white')
credit.bind("<Button-1>", lambda e:webbrowser.open_new_tab("https://linktr.ee/abanand132"))

credit.config(activebackground='blue', activeforeground='black')
credit.grid(row=10, column=2)

image = PhotoImage(file="new3.png")
bottom_img_label = Label(image=image,  bg='white')
bottom_img_label.grid(row=13, column=2)

# Dark/light mode functions
def light_mode_func_home():
    dark_mode_page.light_mode_func_home(window, image_label, website, email, password, label_website, label_email, label_password,
                search, no_of_data, generate, close, clear, detail, label_strength, label, label1, space_label, credit,
                                       create_new_acc, bottom_img_label)
    dark_mode_btn.config(bg='white', foreground='black', command=dark_mode_func_home)
    data['theme'] = 'light'
    with open('basic_info.json', 'w') as d1:
        json.dump(data, d1, indent=4)

def dark_mode_func_home():
    dark_mode_page.dark_mode_func_home(window, image_label, website, email, password, label_website, label_email, label_password,
                search, no_of_data, generate, close, clear, detail, label_strength, label, label1, space_label, credit,
                                       create_new_acc, bottom_img_label)
    dark_mode_btn.config(bg='black', foreground='white', command=light_mode_func_home)
    data['theme'] = 'dark'
    with open('basic_info.json', 'w') as d2:
        json.dump(data, d2, indent=4)


dark_mode_btn = Button(text="🌑", font=('arial', 30), bg='white', foreground='black', borderwidth=0, command=dark_mode_func_home)
dark_mode_btn.grid(row=10, column=4)

# to keep in the desired theme

if data['theme'] == 'light':
    light_mode_func_home()
else:
    dark_mode_func_home()





# Hovering
search.bind("<Enter>", func=lambda e: search.config(background='yellow', foreground='black'))
search.bind("<Leave>", func=lambda e: search.config(background='white', foreground='black'))

add_data.bind("<Enter>", func=lambda e: add_data.config(background='yellow', foreground='black'))
add_data.bind("<Leave>", func=lambda e: add_data.config(background='black', foreground='white'))


window.mainloop()
