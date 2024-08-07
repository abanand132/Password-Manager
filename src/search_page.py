from tkinter import *
import json
import webbrowser
import change_pin_page
import themes
import search
import cipher


str1 = "                        "

# with open('basic_info.json', 'r') as file:
#     data = json.load(file)
def search_window(window, data, my_image):
    search_win = Toplevel()
    search_win.title("Search your password")
    search_win.config(bg='white', padx=30, pady=20)
    search_win.state("zoomed")
    window.iconify()

    def change_pin_func():
        change_pin_page.change_pin_func(window, search_win)

    # ---------------------- Adding Title at Top -----------#

    image_label_search_win = Label(search_win, image=my_image, cursor="hand2")
    image_label_search_win.grid(row=0, column=2)
    image_label_search_win.bind("<Button-1>", lambda e: webbrowser.open_new_tab
                            ("https://theabhishek.tech/projects/pass-manager.html"))

    # labels
    space_label1 = Label(search_win, text=f"{str1}", bg='white', font=('arial', 20))
    space_label1.grid(row=0, column=0)

    # label_search = Label(search_win, bg='white')
    # label_search.grid(row=1, column=2)

    label_search1 = Label(search_win, bg='white')
    label_search1.grid(row=4, column=2)

    label_search2 = Label(search_win, bg='white')
    label_search2.grid(row=5, column=2)

    website_label_search = Label(search_win, text='Website name : ', font=('arial', 13), bg='white')
    website_label_search.grid(row=2, column=1)

    pin_label_search = Label(search_win, text='Enter Pin : ', font=('arial', 13), bg='white', padx=20, pady=10)
    pin_label_search.grid(row=3, column=1)

    # Entries
    website_entry_search = Entry(search_win, width=50, font=('arial', 13), borderwidth=1)
    website_entry_search.config(highlightbackground='black', highlightthickness=1, highlightcolor='red')
    website_entry_search.focus()
    website_entry_search.grid(row=2, column=2)

    pin_entry = Entry(search_win, width=50, font=('arial', 13), show="*", borderwidth=1)
    pin_entry.config(highlightbackground='black', highlightthickness=1, highlightcolor='red')
    pin_entry.grid(row=3, column=2)

    def search_work():
        pin_encrypted_value = data['pin']
        pin_value = cipher.decrypt(pin_encrypted_value)
        search.search_func(pin_entry, pin_value, website_entry_search, search_win, delete_data_btn)

    # Buttons
    search_btn = Button(search_win, text="Search", width=10, font=("consolas", 15, 'bold'), command=search_work)
    search_btn.config(activeforeground='black', activebackground="white", borderwidth=3, bg='black',
                      foreground='white', cursor="hand2")
    search_btn.grid(row=6, column=2)

    change_pin_btn = Button(search_win, text="Change PIN?", font=('arial', 10), bg='white', borderwidth=1,
                            command=change_pin_func, cursor="hand2")
    change_pin_btn.grid(row=6, column=1)


    def clear_options_func():
        # We can clear the content of Entry widget by defining a method delete(0, END) which aims
        # to clear all the content in the range.
        search_win.destroy()
        search_window(window, data, my_image)


    clear_search = Button(search_win, text="Refresh", font=('Consolas', 11), command=clear_options_func)
    clear_search.config(bg='white', activebackground='black', activeforeground='white', borderwidth=2, cursor="hand2")
    clear_search.grid(row=6, column=3)

    def close_function():
        search_win.iconify()
        window.state("zoomed")
        search_win.destroy()


    close_search = Button(search_win, text="Back to Home", font=('Consolas', 11), command=close_function)
    close_search.config(bg='white', activebackground='black', activeforeground='white', borderwidth=2, cursor="hand2")
    close_search.grid(row=0, column=4)

    # decrypt = Button(search_win, text="", bg='white', borderwidth=0, font=('arial', 11), foreground='white')
    # decrypt.grid(row=2, column=4)

    delete_data_btn = Button(search_win, text="", bg='white', borderwidth=0, font=('arial', 11), foreground='white')
    delete_data_btn.grid(row=3, column=4)


    def light_mode_search():
        themes.light_mode_func_search(image_label_search_win, search_win, space_label1,
           label_search1, label_search2, close_search, clear_search, change_pin_btn,
           search_btn, pin_entry, pin_label_search, website_label_search, website_entry_search, delete_data_btn)


        dark_mode_btn_search.config(bg='white', foreground='black', command=dark_mode_search)

        data['theme'] = 'light'
        with open('basic_info.json', 'w') as d1:
            json.dump(data, d1, indent=4)

    def dark_mode_search():
        themes.dark_mode_func_search(image_label_search_win, search_win, space_label1,
                                             label_search1, label_search2, close_search,
                                             clear_search,  change_pin_btn, search_btn, pin_entry, pin_label_search,
                                             website_label_search, website_entry_search, delete_data_btn)

        dark_mode_btn_search.config(bg='#1A2421', foreground='white', command=light_mode_search)

        data['theme'] = 'dark'
        with open('basic_info.json', 'w') as d1:
            json.dump(data, d1, indent=4)

    dark_mode_btn_search = Button(search_win, text="☀/🌙", font=('arial', 18), bg='white', foreground='black',
                                  borderwidth=0, command=dark_mode_search, cursor="hand2", padx=20)
    dark_mode_btn_search.grid(row=0, column=5)

    if data['theme'] == 'light':
        light_mode_search()
    else:
        dark_mode_search()

    search_win.grab_set()
