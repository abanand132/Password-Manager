from tkinter import messagebox
import json
import pyperclip
import encyrpt_message


def strength(password_data, label_strength):
    if 0 < len(password_data) <= 6:
        label_strength.config(text="Weak", font=("Arial", 10, 'bold'), borderwidth=3, foreground="white", bg="red")
    if 6 < len(password_data) <= 10:
        label_strength.config(text="Medium", font=("Arial", 10, 'bold'), borderwidth=3, foreground="white", bg="orange")
    if len(password_data) > 10:
        label_strength.config(text="Strong", font=("Arial", 10, 'bold'), borderwidth=3, foreground="white", bg="green")


def add_data_into_file(website, email, password, label_strength):
    website_data = website.get().lower()
    email_data = email.get()
    password_data = password.get()
    pyperclip.copy(password_data)
    strength(password_data, label_strength)
    new_data = {
        website_data: {
            "email": email_data,
            "password": password_data,
            "status": "normal"
        }
    }
    if len(email_data) != 0 and len(website_data) != 0:
        if len(password_data) > 4:
            if messagebox.askokcancel(title="Confirm Information", message=f"Email : {email_data}\nPassword : {password_data}"
                                            f"\nWebsite : {website_data}\n\nAll Correct ?"):
                try:
                    data_file = open('data_files.json', 'r')
# So what are we doing here ? First open it in 'r' mode. Then read the data from files and then store it in a variable
# 'loading data'. then we update with a new entry or data. In this way, loading data holds the data which is already
# present in the files and with update, it appends the new entry or data. Then we again open the file in the write
# mode and simply load the data i.e., loading data into the json file.
                    loading_data = json.load(data_file)
                    loading_data.update(new_data)
                    data_file = open('data_files.json', 'w')
                    json.dump(loading_data, data_file, indent=4)
                except:
                    data_file = open("data_files.json", 'a')
                    json.dump(new_data, data_file, indent=4)
                data_file.close()  # closing the opened file
                messagebox.showinfo(title="Confirmation", message="Details saved successfully")
        else:
            messagebox.showwarning(message="Entered password is too short. Must be greater than 4 characters")
    else:
        messagebox.showwarning(message="Either your Email address or Website field is empty")

def add_data_into_file_encrypt(website, email, password, label_strength):
    website_data = website.get().lower()
    email_data = encyrpt_message.encrypt(email.get())
    password_data = encyrpt_message.encrypt(password.get())
    strength(password_data, label_strength)
    new_data = {
        website_data: {
            "email": email_data,
            "password": password_data,
            "status": "encrypted"
        }
    }
    if len(email_data) != 0 and len(website_data) != 0:
        if len(password_data) > 4:
            if messagebox.askokcancel(title="Confirm Information",message=f"Email : {email_data}\nPassword : {password_data}"
                                            f"\nWebsite : {website_data}\n\nEncryption enabled ✔\n\nAll Correct ?"):
                try:
                    data_file = open('data_files.json', 'r')
                    loading_data = json.load(data_file)
                    loading_data.update(new_data)
                    data_file = open('data_files.json', 'w')
                    json.dump(loading_data, data_file, indent=4)
                except:
                    data_file = open("data_files.json", 'a')
                    json.dump(new_data, data_file, indent=4)
                data_file.close()
                messagebox.showinfo(title="Confirmation", message="Details saved successfully")
        else:
            messagebox.showwarning(message="Entered password is too short. Must be greater than 4 characters")
    else:
        messagebox.showwarning(message="Either your Email address or Website field is empty")
