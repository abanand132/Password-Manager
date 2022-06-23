from tkinter import messagebox, END, Label, Entry
import json
import decrypt_message
import pyperclip
import advance_search
import multiple_result



# Decrypting data available after successful search
def decryption(website, email, password):
    with open('data_files.json', 'r') as d:
        data = json.load(d)
    website_data = website.get().lower()
    try:
        text1 = email.get()
        text2 = password.get()
        if len(text1) != 0 and len(text2) != 0:
            try:
                if data[website_data]["status"] == "encrypted":
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

def delete_data_func(website):
    website_data = website.get().lower()
    try:
        if messagebox.askyesno(title="Delete", message="Are you want to delete this password ?"
                                                    "\n\nNote : Remember this process can't be reversed"):
            key = website_data
            with open("data_files.json", 'r') as file:
                data_file = json.load(file)
            data_file.pop(key)
            with open("data_files.json", 'w') as file1:
                json.dump(data_file, file1, indent=4)
            messagebox.showinfo(title='Success', message="Password Deleted")

    except KeyError:
        messagebox.showwarning(title='Failed', message='Password already deleted from the database. Or,'
               ' No such data is available in the database to delete\n\nRefresh the page')

    except:
        messagebox.showwarning(title='Failed', message="Unknown Error Occurred! Contact to Developer")


def search_func(pin_entry, pin_value, website, decrypt, window, search_win, delete_data_btn):


    # Sending to decryption function present in search_page.py

    def decrypt_func():
        decryption(website, email_search, password_search)

    def delete_data():
        delete_data_func(website)

    website_data = website.get().lower()
    if pin_entry.get() == pin_value and len(website_data) != 0:

        try:  # reading json file for searching purpose. searching logic below
            with open('data_files.json', 'r') as d:
                data = json.load(d)

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

            # Reading json file just before creating labels and entries. It is the start of searching logic
            k = 0
            for i in data:
                if i == website_data:
                    email_search.insert(0, data[i]['email'])
                    password_search.insert(0, data[i]['password'])
                    pyperclip.copy(password_search.get())
                    messagebox.showinfo(title="Search Result", message=" Data found 👍.\n\nPassword copied to clipboard")
                    k = 1
            if k == 0:
                partial_matched_key = advance_search.advanced_search_func(website_data)
                if partial_matched_key is None:
                    messagebox.showwarning(title="Search Result", message="No such data found")

                elif type(partial_matched_key) == list:
                    if messagebox.askyesno(title="Search Result",
                                           message="We have found multiple results which may satisfy your search.\n\n"
                                                   "Do you want to see result ?"):
                        multiple_result.multiple_result_func(window, partial_matched_key)

                else:
                    if messagebox.askyesno(title="Search Result", message="Exact keyword not found. Do you want to see"
                                                                          " closest matched result ?"):
                        website.delete(0, END)
                        website.insert(0, partial_matched_key)
                        email_search.insert(0, data[partial_matched_key]['email'])
                        password_search.insert(0, data[partial_matched_key]['password'])
                        pyperclip.copy(password_search.get())

        except json.decoder.JSONDecodeError:
            messagebox.showwarning(title='Search Failed', message="You haven't saved any password yet\n\nThank You")

        except :
            messagebox.showwarning(title='Failed', message="Unknown Error Occurred! Contact to Developer")

    elif pin_entry.get() != pin_value and len(pin_entry.get()) > 0:
        messagebox.showwarning(title="Wrong PIN", message="You have entered wrong PIN")

    elif pin_entry.get() == pin_value and len(website_data) == 0:
        messagebox.showwarning(title="Search Failed", message="You can't search with empty website field")

    else:
        messagebox.showwarning(title="Search Failed", message="Enter pin first")
