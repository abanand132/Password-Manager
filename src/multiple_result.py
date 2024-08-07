from tkinter import Toplevel, Scrollbar, Button, END, Text, Label

def multiple_result_func(results_list):
    window2 = Toplevel()
    window2.title("Multiple Results")
    window2.minsize(width=300, height=250)
    window2.config(bg="white", padx=20, pady=20)

    scroll_v = Scrollbar(window2, orient="vertical", width=20)
    scroll_v.grid(row=0, column=1, sticky='ns')
    scroll_h = Scrollbar(window2, orient="horizontal", width=20)
    scroll_h.grid(row=1, column=0, sticky='ew')

    mylist = Text(window2, yscrollcommand=scroll_v.set, width=80, font=('arial', 12), wrap="none", height=15,
                     xscrollcommand=scroll_h.set)
    mylist.grid(row=0, column=0)

    scroll_v.config(command=mylist.yview)
    scroll_h.config(command=mylist.xview)


    for data in results_list:
        data = f"""website-  {data[0]}     email-  {data[1]}    password-  {data[2]}\n"""
        mylist.insert(END, data)
        mylist.insert(END, "-"*120+"\n")

    mylist.config(state="disabled")

    def close_func():
        window2.destroy()
        # window.state("zoomed")

    label = Label(window2, text="", bg="white", padx=10)
    label.grid(row=0, column=2)
    close = Button(window2, text="close", font=("arial", 12), command=close_func)
    close.grid(row=0, column=3)
    window2.grab_set()
