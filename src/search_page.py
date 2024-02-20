from tkinter import messagebox, END, Label, Entry
import decrypt_message
import pyperclip
import multiple_result
from database import Db

# database object
obj = Db()

# Decrypting data available after successful search
def decryption(website_data, email, password):
    try:
        text1 = email.get()
        text2 = password.get()
        if len(text1) != 0 and len(text2) != 0:
            try:
                if obj.data_status(website_data):
                    decrypted_email_data = decrypt_message.decrypt(text1)
                    decrypted_password_data = decrypt_message.decrypt(text2)
                    email.delete(0, END)
                    password.delete(0, END)
                    email.insert(0, decrypted_email_data)
                    password.insert(0, decrypted_password_data)
                    pyperclip.copy(password.get())
                    # k = 0
                else:
                    messagebox.showwarning(title="Request failed 🛑", message="These data are not encrypted.")
            except ValueError:
                messagebox.showwarning(title="Request failed 🛑", message="Data is already decrypted")
        else:
            messagebox.showinfo(message="Enough Data is not Available")

    except KeyError:
        messagebox.showwarning(title='Failed', message='No such data available to decrypt')
    except:
        messagebox.showwarning(title='Failed', message="Unknown Error Occurred! Inform to Developer")

def delete_data_func(website_data):
    try:
        if messagebox.askyesno(title="Delete", message="Are you want to delete this password ?"
                                                    "\n\nNote : Remember this process can't be reversed"):

            if obj.delete_data(website_data):
                messagebox.showinfo(title='Success', message="Password Deleted")


    except:
        messagebox.showwarning(title='Failed', message="Unknown Error Occurred! Contact to Developer")


def search_func(pin_entry, pin_value, website, decrypt, window, search_win, delete_data_btn):
    website_data = website.get().lower()

    # Sending to decryption function present in search_page.py

    def decrypt_func():
        decryption(website_data, email_search, password_search)

    def delete_data():
        delete_data_func(website_data)


    if pin_entry.get() == pin_value and len(website_data) != 0:

        # try:  # reading json file for searching purpose. searching logic below

            decrypt.config(text="Decrypt", command=decrypt_func, borderwidth=2)
            delete_data_btn.config(text="Delete Password", command=delete_data, borderwidth=2)

            # deleting text and customizing pin entry box so that we can hide it beside email entry box
            pin_entry.delete(0, END)
            pin_entry.config(width=0, borderwidth=0)
            # Again creating labels and entry boxes to display emails and passwords associated with it.
            label_email_search = Label(search_win, text="Email/Username : ", bg="white", font=("arial", 13))
            label_email_search.grid(row=3, column=1)

            label_password_search = Label(search_win, text="Password : ", bg="white", font=("arial", 13))
            label_password_search.config(padx=50)
            label_password_search.grid(row=4, column=1)

            email_search = Entry(search_win, width=50, font=('arial', 13), borderwidth=1)
            email_search.config(highlightbackground='black', highlightthickness=1, highlightcolor='red')
            email_search.grid(row=3, column=2)

            password_search = Entry(search_win, width=50, font=('arial', 13), borderwidth=1)
            password_search.config(highlightbackground='black', highlightthickness=1, highlightcolor='red')
            password_search.grid(row=4, column=2)


            result = obj.search_password(website=website_data)

            if len(result) == 0:
                messagebox.showinfo(title="Result", message="No records found!!")

            elif len(result) == 1:
                email_search.insert(0, result[0][1])
                password_search.insert(0, result[0][2])
                pyperclip.copy(password_search.get())
                messagebox.showinfo(title="Search Result", message=" Data found 👍.\n\nPassword copied to clipboard")

            else:
                if messagebox.askyesno(title="Search Result",
                                       message="We have found multiple results which may satisfy your search.\n\n"
                                               "Do you want to see result ?"):
                    multiple_result.multiple_result_func(window, result)


        # except:
        #     messagebox.showwarning(title='Failed', message="Unknown Error Occurred! Contact to Developer")

    elif pin_entry.get() != pin_value and len(pin_entry.get()) > 0:
        messagebox.showwarning(title="Wrong PIN", message="You have entered wrong PIN")

    elif pin_entry.get() == pin_value and len(website_data) == 0:
        messagebox.showwarning(title="Search Failed", message="You can't search with empty website field")

    else:
        messagebox.showwarning(title="Search Failed", message="Enter pin first")
