import json
import time
from tkinter import Toplevel, Label, Button, Entry, messagebox
from email_page import send_email
import encyrpt_message
import decrypt_message

def change_pin_func(window, search_win):
    pin_window = Toplevel()
    pin_window.title("Change PIN")
    pin_window.config(bg='white', padx=20, pady=20, width=400, height=400)
    # window.iconify()

    heading = Label(pin_window, text='Change PIN', font=('Consolas', 20), foreground='red', bg='white')
    heading.grid(row=0, column=1)

    label1 = Label(pin_window, text="", bg='white', pady=10)
    label1.grid(row=1, column=1)

    email_label = Label(pin_window, text="Email :  ", bg='white', font=('arial', 13))
    email_label.grid(row=2, column=0)

    email_entry = Entry(pin_window, width=40, font=('arial', 14), bg='white')
    email_entry.focus()
    email_entry.grid(row=2, column=1)

    label2 = Label(pin_window, text="", bg='white', pady=10)
    label2.grid(row=3, column=1)

    label3 = Label(pin_window, text="", bg='white', pady=10)
    label3.grid(row=5, column=1)

    label4 = Label(pin_window, text="", bg='white', pady=10)
    label4.grid(row=7, column=1)

    notification = Label(pin_window, text="", bg='white', pady=10)
    notification.grid(row=6, column=1)

    # Functions
    def send_code_func():
        with open('basic_info.json', 'r') as data:
            loading_data = json.load(data)
        if email_entry.get() == decrypt_message.decrypt(loading_data['email']):
            pin = send_email()
            if pin:
                x = "Email sent successfully. Check spam box in case you haven't found email in your inbox"
                notification.config(text=f"{x}", bg='black', foreground='white', font=('arial', 10, 'bold'))
                loading_data['code'] = pin
                with open('basic_info.json', 'w') as data:  # updating code in json file
                    json.dump(loading_data, data, indent=4)
        else:
            messagebox.showwarning(title='Failed', message='You have entered wrong email')


    # Buttons
    send_code_btn = Button(pin_window, text='Send Code', font=('arial', 13), bg='green', foreground='white')
    send_code_btn.config(command=send_code_func)
    send_code_btn.grid(row=4, column=1)

    code_label = Label(pin_window, text='Code : ', font=('arial', 12), bg='white')
    code_label.grid(row=8, column=0)

    code_entry = Entry(pin_window, width=20, font=('arial', 14), bg='white')
    code_entry.grid(row=8, column=1)

    def submit_btn_func():
        code_sent_to_mail = code_entry.get()
        with open('basic_info.json', 'r') as data:  # loading code which is saved in the basic_info json file
            loading_data = json.load(data)
        code_save_in_file = loading_data['code']

        if code_save_in_file == code_sent_to_mail:
            modification_func()  # it deletes/customize everything in the window
        else:
            messagebox.showwarning(title='Error', message='Wrong Code')

    submit_btn = Button(pin_window, text="Enter", font=('arial', 12, 'bold'), bg='red', foreground='white')
    submit_btn.config(command=submit_btn_func)
    submit_btn.grid(row=8, column=2)

    def modification_func():
        email_label.destroy()
        email_entry.destroy()
        label3.destroy()
        label4.destroy()
        send_code_btn.destroy()
        code_label.destroy()
        code_entry.destroy()
        submit_btn.destroy()
        notification.destroy()
        heading.config(text="Enter New PIN")
        new_pin_label = Label(pin_window, text="New PIN : ", bg='white', font=('arial', 12))
        new_pin_label.grid(row=2, column=0)
        new_pin_entry = Entry(pin_window, width=40, font=('arial', 14), bg='white')
        new_pin_entry.focus()
        new_pin_entry.grid(row=2, column=1)
        submit_pin_btn = Button(pin_window, text="Save PIN", font=('arial', 12, 'bold'), bg='red',
                                foreground='white')

        def save_pin_func():
            new_pin = new_pin_entry.get()
            with open('basic_info.json', 'r') as data_file:
                loading_data = json.load(data_file)
            loading_data['pin'] = encyrpt_message.encrypt(new_pin)
            loading_data['code'] = ""
            with open('basic_info.json', 'w') as data:  # updating code in json file
                json.dump(loading_data, data, indent=4)
            notify = Label(pin_window, text='PIN Changed!!', bg='white', font=('consolas', 16), pady=20)
            notify.grid(row=5, column=1)
            messagebox.showinfo(title="Need Restart", message="Need to restart the application to complete the "
                                                                 "process of recent changes")
            time.sleep(1)
            search_win.destroy()
            window.destroy()

        submit_pin_btn.config(command=save_pin_func)
        submit_pin_btn.grid(row=4, column=1)

    pin_window.grab_set()
