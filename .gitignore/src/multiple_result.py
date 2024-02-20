from tkinter import Toplevel, Label, Button

def multiple_result_func(window, results_list):
    window2 = Toplevel()
    window2.title("Multiple Results")
    window2.minsize(width=300, height=200)
    window2.config(bg="white", padx=10, pady=20)

    website_label = Label(window2, text="Website", bg='white', foreground='black', font=('arial', 13), pady=20)
    website_label.grid(row=0, column=0)
    email_label = Label(window2, text="Email/Username", bg='white', foreground='black', font=('arial', 13), padx=20)
    email_label.grid(row=0, column=1)
    password_label = Label(window2, text="Password", bg='white', foreground='black', font=('arial', 13), padx=20)
    password_label.grid(row=0, column=2)
    status_label = Label(window2, text="Status", bg='white', foreground='black', font=('arial', 13))
    status_label.grid(row=0, column=3)


    x = 1
    for data in results_list:
        label1 = Label(window2, text=f"{data[0]}", bg="white", font=("arial", 12), foreground="red")
        label1.grid(row=x, column=0)
        label2 = Label(window2, text=f"{data[1]}", bg="white", font=("arial", 12), foreground="blue")
        label2.grid(row=x, column=1)
        label3 = Label(window2, text=f"{data[2]}", bg="white", font=("arial", 12))
        label3.grid(row=x, column=2)
        label4 = Label(window2, text=f"{data[3]}", bg="white", font=("arial", 12))
        label4.grid(row=x, column=3)

        x += 1

    space = Label(window2, text="", bg="white")
    space.grid(row=x, column=0)

    def close_func():
        window2.destroy()
        window.state("zoomed")
    close = Button(window2, text="close", font=("arial", 12), command=close_func)
    close.grid(row=x+1, column=0)
    window2.grab_set()
