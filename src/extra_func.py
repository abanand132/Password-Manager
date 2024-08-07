
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

import database

def create_popup(window):
    obj = database.Db()

    def export_password():
        df = obj.export_pass()
        obj.close_connection()
        path = filedialog.askdirectory()
        if path:
            df.to_csv(f"{path}/password.csv", index=False)
            messagebox.showinfo(title="Success", message="Password Exported")

        popup.destroy()
        window.state("zoomed")


    def import_password():
        path = filedialog.askopenfile(title="Select password.csv file", filetypes=[("CSV files", "*.csv")])
        if obj.import_pass(path):
            messagebox.showinfo(title="Success", message="Password Imported")
        else:
            messagebox.showerror(title="Failed", message="Failed!")
        obj.close_connection()
        popup.destroy()

    def delete_all_password():
        if messagebox.askyesno(title="Delete All Passwords", message="Are you really want to "
                                                            "delete all your passwords ?"):
            if obj.delete_all_pass():
                messagebox.showinfo(title="Success", message="All passwords are deleted")
                obj.close_connection()
                popup.destroy()

    popup = Toplevel()
    popup.title("Import/Export Your Passwords")
    popup.config(bg='white', padx=20, pady=20)
    popup.minsize(width=350, height=100)

    button1 = Button(popup, text="Import Password", bg='white', command=import_password, cursor="hand2")
    button1.pack(pady=10)

    button2 = Button(popup, text="Export Password", bg='white', command=export_password, cursor="hand2")
    button2.pack(pady=10)

    button3 = Button(popup, text="Delete All Password", bg='white', command=delete_all_password, cursor="hand2")
    button3.pack(pady=10)

    popup.grab_set()
