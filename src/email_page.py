# Python code to illustrate Sending mail with attachments
# from your Gmail account
import json
from tkinter import messagebox
import random
import smtplib
import ssl
import cipher
from email.message import EmailMessage

def code():
    list = []
    for i in range(6):
        list.append(str(random.randint(0, 9)))
    list1 = "".join(list)
    return list1

def send_email():
    pin = code()
    try:
        with open("basic_info.json", 'r') as data:
            loading_data = json.load(data)
        # Define email sender and receiver
        email_sender = 'yourfriend0112@gmail.com'
        email_password = 'rlzxgyssmgxzxcdx'
        email_receiver = cipher.decrypt(loading_data['email'])

        # Mail for Sending OTP
        otp_subject = 'PIN Reset Code'

        otp_body = (f"This is a mail from 'Password Manager'.\n\nAs requested by you, your code : {pin}\n\nYou can"
                f" watch demo video or read about features of password manager here - https://theabhishek.tech/"
                f"projects/pass-manager.html (highly recommended) \n\nIf you have any"
               f" suggestion or feedback for me then simple reply to this mail. Or,\nYou can also reach out to me :"
               f"https://theabhishek.tech\nHope you love the application and will continue to use it.\n\n"
               f"NOTE : All your data is saved in your local device so it is completely safe. You don't need to rely "
               f"on any third party services.\nThank You\n\nRegards\nAbhishek")


        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = otp_subject
        em.set_content(otp_body)

        # Add SSL (layer of security)
        context = ssl.create_default_context()

        # Log in and send the email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())

        messagebox.showinfo(title='Success', message='Email sent successfully')
        return pin
    except:
        messagebox.showwarning(title='Failed', message="Error! Check your internet connection")


def welcome_mail(email_receiver):
    # Define email sender and receiver
    email_sender = 'yourfriend0112@gmail.com'
    email_password = 'rlzxgyssmgxzxcdx'

    welcome_subject = 'Thank You for Using Password Manager'

    welcome_body = (f"This is a mail from 'Password Manager'. Thank you for using our app.\n\n"
                    f"To get started quickly and make the most of our features, please take a moment to watch our demo "
                    f"videos. They’ll guide you through the installation process and show you how to use the app "
                    f"effectively.\n\nDemo Videos - "
                    f"https://theabhishek.tech/projects/pass-manager.html (highly recommended) \n\n"
                    f"If you have any suggestion or feedback for me then simple reply to this mail or "
                    f"you can also reach out to me - https://theabhishek.tech\n\n"
                    f"Hope you love the application and will continue to use it.\n\n"
                    f"NOTE : All your data is saved in your local device so it is completely safe. "
                    f"You don't need to rely on any third party services.\nThank You\n\nRegards\nAbhishek Anand")


    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = welcome_subject
    em.set_content(welcome_body)

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

    # messagebox.showinfo(title='Success', message='Email sent successfully')
