from cryptography.fernet import Fernet
import os
from tkinter import messagebox


# getting the key from the environment variable
key = os.getenv('ENCRYPTION_KEY_PASS_MANAGER')


def encrypt(message: str):
    """
    It takes string as input and returns encrypted text in bytes
    :param message: plain text
    :return: encrypted text in bytes
    """
    # creating fernet object
    try:
        cipher = Fernet(key.encode())
        # cipher_text is in bytes
        cipher_text = cipher.encrypt(message.encode())
        return cipher_text.decode()
    except AttributeError:
        messagebox.showerror(title="Failed", message="Secret-key is not available as environment variable")

def decrypt(cipher_text: str):
    """
    It takes encrypted/cipher text as input and return plain text
    :param cipher_text: encrypted text in strings
    :return: plain/decrypted text as strings
    """
    # creating fernet object
    try:
        cipher = Fernet(key.encode())
        plain_text = cipher.decrypt(cipher_text.encode()).decode()
        return plain_text
    except AttributeError:
        messagebox.showerror(title="Failed", message="Secret-key is not available as environment variable")
