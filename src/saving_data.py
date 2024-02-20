from tkinter import messagebox
import json
import pyperclip
import encyrpt_message
from database import Db

# creating Db class object
obj = Db()

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

    if len(email_data) != 0 and len(website_data) != 0:
        if len(password_data) > 4:
            if messagebox.askokcancel(title="Confirm Information", message=f"Email : {email_data}\nPassword : {password_data}"
                                            f"\nWebsite : {website_data}\n\nAll Correct ?"):

                obj.insert_new_info(website=website_data, email=email_data,
                                    password=password_data, status="normal")
        else:
            messagebox.showwarning(message="Entered password is too short. Must be greater than 4 characters")
    else:
        messagebox.showwarning(message="Either your Email address or Website field is empty")

def add_data_into_file_encrypt(website, email, password, label_strength):
    website_data = website.get().lower()
    email_data = encyrpt_message.encrypt(email.get())
    password_data = encyrpt_message.encrypt(password.get())
    strength(password_data, label_strength)

    if len(email_data) != 0 and len(website_data) != 0:
        if len(password_data) > 4:
            if messagebox.askokcancel(title="Confirm Information", message=f"Email : {email_data}\nPassword : "
                        f"{password_data}\nWebsite : {website_data}\n\nEncryption enabled ✔\n\nAll Correct ?"):

                obj.insert_new_info(website=website_data, email=email_data,
                                    password=password_data, status="encrypted")
        else:
            messagebox.showwarning(message="Entered password is too short. Must be greater than 4 characters")
    else:
        messagebox.showwarning(message="Either your Email address or Website field is empty")
