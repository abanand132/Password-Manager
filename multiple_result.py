from tkinter import Toplevel, Label, Button
import json

def multiple_result_func(window, results_list):
    window2 = Toplevel()
    window2.title("Multiple Results")
    window2.minsize(width=300, height=200)
    window2.config(bg="white", padx=10, pady=20)
    with open("data_files.json", 'r') as data_file:
        data = json.load(data_file)

    website_label = Label(window2, text="Website", bg='white', foreground='black', font=('arial', 13), pady=20)
    website_label.grid(row=0, column=0)
    email_label = Label(window2, text="Email/Username", bg='white', foreground='black', font=('arial', 13), padx=20)
    email_label.grid(row=0, column=1)
    password_label = Label(window2, text="Password", bg='white', foreground='black', font=('arial', 13))
    password_label.grid(row=0, column=2)


    x = 1
    for i in results_list:
        label1 = Label(window2, text=f"{i}", bg="white", font=("arial", 12), foreground="red")
        label1.grid(row=x, column=0)
        label2 = Label(window2, text=f"{data[i]['email']}", bg="white", font=("arial", 12), foreground="blue")
        label2.grid(row=x, column=1)
        label3 = Label(window2, text=f"{data[i]['password']}", bg="white", font=("arial", 12))
        label3.grid(row=x, column=2)

        x += 1

    space = Label(window2, text="", bg="white")
    space.grid(row=x, column=0)

    def close_func():
        window2.destroy()
        window.state("zoomed")
    close = Button(window2, text="close", font=("arial", 12), command=close_func)
    close.grid(row=x+1, column=0)
    window2.grab_set()
