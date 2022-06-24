# importing subprocess module
import subprocess
from tkinter import messagebox

# importing urllib.requests for internet checking functions
import urllib.request


# initializing host to gfg.
def connect(host='https://www.geeksforgeeks.org/'):
    # trying to open gfg
    try:
        urllib.request.urlopen(host)
        return True

    # trying to catch exception when internet is not ON.
    except:
        return False


def main(module_name):
    # updating pip to latest version
    subprocess.run('python -m pip install --upgrade pip')

    # commanding terminal to pip install
    p = subprocess.run('pip3 install ' + module_name)

    # internet off
    if p.returncode == 1 and connect() == False:
        messagebox.showwarning(title='Failed', message="Error!!\n\nCheck Internet connection")

    # Every thing worked fine
    elif p.returncode == 0:
        if messagebox.askokcancel(title="Restart Application", message="We installed some required library to "
                                                                       "run this application.\nSo, you need to restart the application to complete the installation"
                                                                       " process.\n\nThank you"):
            exit()
    # Name of module wrong
    elif p.returncode == 1 and connect():
        messagebox.showwarning(title='Failed', message="error!! occurred check\nName of module")
