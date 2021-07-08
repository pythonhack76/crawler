from tkinter import Menu, Message, Text, Tk, mainloop, LEFT, TOP
from tkinter.constants import BOTTOM, END
from tkinter.ttk import *
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from bs4 import BeautifulSoup
from tkinter import messagebox
import requests

#gestione messaggi
def showMessage():
    messagebox.showinfo("showinfo", "Informazioni")


def clearAll(): 

    #cancella i contenuti delle input type
    urlField.delete(0, END)

def checkError(): 

    if(urlField.get() == ""):
        messagebox.showerror("campo non compilato!")

        clearAll()

        return -1

# Driver Code
if __name__ == "__main__" :

    window = tk.Tk()
    window.geometry('600x480')
    window.title("SEO Check by LR")
    window.iconphoto(False, tk.PhotoImage(file='pendrive.png'))

    w = Label(window, text ='Software SEO URL Checking', font = "50") 
    w.grid(row = 0 , column = 0)

    frame = Frame(window)
    frame.grid()

    # Create a Day : label
    url = Label(window, text = "url", background = "light green", foreground = "red")
    urlField = Entry(window)

    url.grid(row =1, column =1 )
    urlField.grid(row = 1, column = 2)

    #bottoni
    b1_button = Button(frame, text="Chiudi", command=window.destroy)
    b1_button.grid( row = 3, column = 3)

    erase_button = Button(frame, text="Cancella", command=clearAll)
    erase_button.grid(row = 3, column = 2)

    # Creating Menubar
    menubar = Menu(window)
    
    # Adding File Menu and commands
    file = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='File', menu = file)
    file.add_command(label ='New File', command = None)
    file.add_command(label ='Open...', command = None)
    file.add_command(label ='Save', command = None)
    file.add_separator()
    file.add_command(label ='Exit', command = window.destroy)
    
    
    # Adding Help Menu
    help_ = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Help', menu = help_)
    help_.add_command(label ='Tk Help', command = None)
    help_.add_command(label ='Demo', command = None)
    help_.add_separator()
    help_.add_command(label ='About SEO Check', command = None)



    window.config(menu = menubar)
    window.mainloop()