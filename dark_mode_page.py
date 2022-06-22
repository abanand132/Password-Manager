
def dark_mode_func_home(window, image_label, website, email, password, label_website, label_email, label_password,
                search, no_of_data, generate, close, clear, detail, label_strength, label, label1, space_label, credit,
                                       create_new_acc, bottom_img_label):
    window.config(bg="black")
    image_label.config(bg="black")
    website.config(bg='black', foreground='white', insertbackground='white', highlightbackground='cyan')
    email.config(bg='black', foreground='white', insertbackground='white', highlightbackground='cyan')
    password.config(bg='black', foreground='white', insertbackground='white', highlightbackground='cyan')
    label_website.config(bg='black', foreground='yellow')
    label_email.config(bg='black', foreground='yellow')
    label_password.config(bg='black', foreground='yellow')
    search.config(bg='yellow', foreground='black')
    search.bind("<Enter>", func=lambda e: search.config(background='cyan', foreground='black'))
    search.bind("<Leave>", func=lambda e: search.config(background='yellow', foreground='black'))
    no_of_data.config(bg="black", foreground='yellow')
    generate.config(bg='yellow', foreground='black')
    close.config(bg='yellow', foreground='black')
    clear.config(bg='yellow', foreground='black')
    detail.config(bg='yellow', foreground='black')
    credit.config(bg='yellow', foreground='black')
    create_new_acc.config(bg='yellow', foreground='black')
    bottom_img_label.config(bg='black')
    label_strength.config(bg='black')
    label.config(bg='black')
    label1.config(bg='black')
    space_label.config(bg='black')

def light_mode_func_home(window, image_label, website, email, password, label_website, label_email, label_password,
                search, no_of_data, generate, close, clear, detail, label_strength, label, label1, space_label, credit,
                                       create_new_acc, bottom_img_label):
    window.config(bg="white")
    image_label.config(bg="white")
    website.config(bg='white', foreground='black', insertbackground='black', highlightbackground='black')
    email.config(bg='white', foreground='black', insertbackground='black', highlightbackground='black')
    password.config(bg='white', foreground='black', insertbackground='black', highlightbackground='black')
    label_website.config(bg='white', foreground='black')
    label_email.config(bg='white', foreground='black')
    label_password.config(bg='white', foreground='black')
    search.config(bg='white', foreground='black')
    search.bind("<Enter>", func=lambda e: search.config(background='yellow', foreground='black'))
    search.bind("<Leave>", func=lambda e: search.config(background='white', foreground='black'))
    no_of_data.config(bg="white", foreground='black')
    generate.config(bg='white', foreground='black')
    close.config(bg='white', foreground='black')
    clear.config(bg='white', foreground='black')
    detail.config(bg='white', foreground='black')
    credit.config(bg='white', foreground='black')
    create_new_acc.config(bg='white', foreground='black')
    bottom_img_label.config(bg='white')
    label_strength.config(bg='white')
    label.config(bg='white')
    label1.config(bg='white')
    space_label.config(bg='white')


def dark_mode_func_search(image_label, search_win, space_label1, label_search, label_search1, label_search2, close_search,
        clear_search, create_new_acc_search, change_pin_btn, search_btn, pin_entry, pin_label_search,
                                  website_label_search, website_entry_search, decrypt, delete_data_btn):
    image_label.config(bg='black')
    search_win.config(bg='black')
    space_label1.config(bg='black')
    label_search.config(bg='black')
    label_search1.config(bg='black')
    label_search2.config(bg='black')
    website_label_search.config(bg='black', foreground='yellow')
    pin_label_search.config(bg='black', foreground='yellow')
    close_search.config(bg='yellow', foreground='black')
    clear_search.config(bg='yellow', foreground='black')
    create_new_acc_search.config(bg='yellow', foreground='black')
    change_pin_btn.config(bg='yellow', foreground='black')
    search_btn.config(bg='yellow', foreground='black')
    decrypt.config(bg='black', foreground='white')
    delete_data_btn.config(bg='black', foreground='white')
    website_entry_search.config(bg='black', foreground='white', insertbackground='white', highlightbackground='cyan')
    pin_entry.config(bg='black', foreground='white', insertbackground='white', highlightbackground='cyan')


def light_mode_func_search(image_label, search_win, space_label1, label_search, label_search1, label_search2, close_search,
        clear_search, create_new_acc_search, change_pin_btn, search_btn, pin_entry, pin_label_search,
                                  website_label_search, website_entry_search, decrypt, delete_data_btn):
    image_label.config(bg='white')
    search_win.config(bg='white')
    space_label1.config(bg='white')
    label_search.config(bg='white')
    label_search1.config(bg='white')
    label_search2.config(bg='white')
    website_label_search.config(bg='white', foreground='black')
    pin_label_search.config(bg='white', foreground='black')
    close_search.config(bg='white', foreground='black')
    clear_search.config(bg='white', foreground='black')
    create_new_acc_search.config(bg='white', foreground='black')
    change_pin_btn.config(bg='white', foreground='black')
    search_btn.config(bg='black', foreground='white')
    decrypt.config(bg='white', foreground='black')
    delete_data_btn.config(bg='white', foreground='black')
    website_entry_search.config(bg='white', foreground='black', insertbackground='black', highlightbackground='black')
    pin_entry.config(bg='white', foreground='black', insertbackground='black', highlightbackground='black')
