# Python code to illustrate Sending mail with attachments
# from your Gmail account
import json
from tkinter import messagebox
import random
import decrypt_message

def code():
    list = []
    for i in range(6):
        list.append(str(random.randint(0, 9)))
    list1 = "".join(list)
    return list1

def send_email():
    import smtplib
    import ssl
    from email.message import EmailMessage
    pin = code()
    try:
        with open("basic_info.json", 'r') as data:
            loading_data = json.load(data)
        # Define email sender and receiver
        email_sender = 'yourfriend0112@gmail.com'
        email_password = 'rlzxgyssmgxzxcdx'
        email_receiver = decrypt_message.decrypt(loading_data['email'])

        # Set the subject and body of the email
        subject = 'PIN Reset Code'

        body = f"This is a mail from 'Password Manager'.\n\nAs requested by you, your code : {pin}\n\nIf you have any" \
               f" suggestion or feedback for me then simple reply to this mail. Or,\nYou can also reach out to me :" \
               f"https://linktr.ee/abanand132.\n\nHope you love the application and will continue to use it.\n\n" \
               f"NOTE : All your data is saved in your local device so it is completely safe. You don't need to rely " \
               f"on any third party services.\nThank You\n\nRegards\nAbhishek"

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)

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




