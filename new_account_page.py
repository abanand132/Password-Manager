import json
from tkinter import *
from tkinter import messagebox

import decrypt_message
import encyrpt_message
import email_page


def create_account_func(home_window):
    account_win = Toplevel()
    account_win.title("Create Account")
    account_win.config(bg='white', padx=20)
    account_win.minsize(width=450, height=350)

    heading = Label(account_win, text="Create Account", bg='white', foreground='red', font=('arial', 20), pady=10)
    heading.grid(row=0, column=1)

    email_label = Label(account_win, text="Email :   ", font=('arial', 12), bg="white", pady=10)
    email_label.grid(row=1, column=0)

    email = Entry(account_win, width=30, font=('arial', 13), borderwidth=1, highlightcolor='black', highlightthickness=1,
                  highlightbackground='red')
    email.grid(row=1, column=1)

    pin_label = Label(account_win, text="PIN :   ", font=('arial', 12), bg="white")
    pin_label.grid(row=2, column=0)

    pin = Entry(account_win, width=15, font=('arial', 13), borderwidth=3)
    pin.grid(row=2, column=1)

    message = "You are not actually creating any account here.\nSoftware just need your Email so that it can\n" \
              "be used to reset your PIN."
    message_label = Label(account_win, text=message, font=("arial", 11), bg="white", pady=30)
    message_label.grid(row=5, column=1)

    save_button = Button(account_win, text="SAVE", font=("arial", 12, 'bold'), bg="green", foreground="white")
    save_button.grid(row=4, column=1)

    var = IntVar(value=1)

    with open('basic_info.json', 'r') as data:
            data = json.load(data)
    if len(data['email']) > 0:
        heading.config(text="Update Account")
        email_label.config(text='Current Email : ')
        pin_label.destroy()
        message_label.destroy()
        pin.destroy()
        save_button.config(text='Send Code')
        var.set(0)


    label = Label(account_win, text='', bg='white')
    label.grid(row=3, column=1)

    def save_func():
        with open("basic_info.json", "w") as file:
            if len(email.get()) != 0 and len(pin.get()) != 0:
                data = {
                        "email": encyrpt_message.encrypt(email.get()),
                        "pin": encyrpt_message.encrypt(pin.get()),
                        "theme": "light",
                        "code": ""
                    }
                json.dump(data, file, indent=4)
                if messagebox.showinfo(title="Success",
                                       message="Account created successfully\n\nPlease restart the application"
                                               " to enable recent changes!"):
                    account_win.destroy()
                    home_window.destroy()
            else:
                messagebox.showwarning(title="Error", message="You can't leave PIN or Email fields empty")

    def update_func():
        with open("basic_info.json", "r") as data_file:
            load_data = json.load(data_file)
        if len(email.get()) > 0 and decrypt_message.decrypt(load_data['email']) == email.get():
            save_button.destroy()
            email_label.config(text='New Email : ')
            email.delete(0, END)
            code_sent_to_email = email_page.send_email()  # calling email function which sent code

            load_data['code'] = encyrpt_message.encrypt(code_sent_to_email)  # encrypting code that is sent
                                                                             # to email and save in json file
            with open('basic_info.json', 'w') as data3:  # updating 'code' in json file
                json.dump(load_data, data3, indent=4)

            code_label = Label(account_win, text='Code : ', font=('arial', 12), bg='white')
            code_label.grid(row=6, column=0)

            code_entry = Entry(account_win, width=20, font=('arial', 14), bg='white', highlightcolor='black',
                               highlightbackground='red', highlightthickness=1)
            code_entry.grid(row=6, column=1)

            # if len(email.get()) > 0:
            def submit_btn_func():
                with open("basic_info.json", "r") as data_file1:
                    load_data1 = json.load(data_file1)
                code_save_in_file = load_data1['code']
                if code_entry.get() == decrypt_message.decrypt(code_save_in_file):
                    load_data1['email'] = encyrpt_message.encrypt(email.get())
                    load_data1['code'] = ""
                    with open('basic_info.json', 'w') as data4:  # updating code in json file
                        json.dump(load_data1, data4, indent=4)
                    if messagebox.showinfo(title="Success", message="Email successfully updated\n\nPlease restart the application"
                                                                 " to enable recent changes!"):

                        account_win.destroy()
                        home_window.destroy()
                else:
                    messagebox.showwarning(title='Failed', message='Wrong Code!')

            submit_btn = Button(account_win, text="Submit", font=('arial', 12, 'bold'), bg='red', foreground='white')
            submit_btn.config(command=submit_btn_func)
            submit_btn.grid(row=8, column=2)
        else:
            messagebox.showwarning(title="Error", message="Wrong Email! Details not matched")


    # save_button declaration above
    if var.get() == 1:
        save_button.config(command=save_func)
    else:
        save_button.config(command=update_func)





    account_win.grab_set()
