#####Expect tons of spaghetti code , plus i doubt you even read this
#####Just copy and paste it into google to see if i copy and pasted

#All needed modules here
from tkinter import *

def reguser():

    username_info = username.get()
    password_info = password.get()

    file=open(username_info+".txt", "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(regmenu, text = "Registration Complete", fg = "green" ,font = ("calibri", 12)).pack()

def register(): # all the account data handling , plz send help
    global regmenu
    regmenu = Toplevel(menu)
    regmenu.title("Register")
    regmenu.geometry("350x300")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(regmenu, text = "Registeration").pack()
    Label(regmenu, text = "").pack()
    Label(regmenu, text = "Username ' ").pack()
    username_entry = Entry(regmenu, textvariable = username)
    username_entry.pack()
    Label(regmenu, text = "Password ' ").pack()
    password_entry = Entry(regmenu, textvariable = password)
    password_entry.pack()
    Label(regmenu, text = "").pack()
    Button(regmenu, command = reguser, text = "Register", width = 15, height = 2).pack()

def login(): #all your passwords are in plain text , facebook was my inspiration
    print("someone is trying to guess a password")


def login_menu():    #Basically the login system ui , the rest of the comments can be up to your imagination because ill probly forget to comment things 3 hours in
    global menu




    menu = Tk()
    menu.geometry("350x300")
    menu.title("Python Music Quiz")
    Label(text = "Python Music Quiz", bg = "grey", width = "350", height = "4", font = ("Calibri", 13)).pack()
    Label(text = "").pack() #Blank Spacer 900000000
    Button(text = "Login", command = login, height = "4", width = "40").pack()
    Label(text = "").pack() #Blank Spacer 900000000
    Button(text = "Register", command = register, height = "4", width = "40").pack()


    menu.mainloop()
    
login_menu()
