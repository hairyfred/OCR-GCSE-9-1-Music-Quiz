#####Expect tons of spaghetti code , plus i doubt you even read this
#####Just copy and paste it into google to see if i copy and pasted

#All needed modules here
from tkinter import *
import os
import random
import time


#Gonna be all the awnsers here so stop cheating boi

questions = ['Q0', 'Q1', 'Q2', 'Q3', 'Q4']
questionsorig = ['Q0', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9']
questiontot = 0
endme = 1




#Legit its a tkinter massacare in this section
def killcorrectmenu():
    correctmenu.destroy()
def killwrongmenu():
    wrongmenu.destroy()
def killfailedmenu():
    failedmenu.destroy()
def killsessionmenu():
    sessionmenu.destroy()
def killloginmenu():
    logmenu.destroy()
def killregmenu():
    regmenu.destroy()
def killquestion():
    quizmenu.destroy()
#rip

test123 = 1

a = True


    

def actualquiz():
    random.shuffle(questions)
    global quizmenu
    global questiontot
    questiontot = 0
    while True:
        if questions[0] == 'Q0':
            print("Question 1 Has been Selected")
            del questions[0]
            questiontot += 1
            quizmenu = Toplevel(menu)
            quizmenu.title("Quiz")
            quizmenu.geometry("512x512")
            test_entry = Entry(quizmenu, show="", textvariable = test123)
            test_entry.pack()
            Button(quizmenu, text = "Quit").pack()
 #           test_info = test123.get()
 #           if test_info == 0:
 #               print("wtf")
 #           else:
 #               print("how is this working")     
            print("XDLMAO1")
            time.sleep(1)
            break
            time.sleep(1)
            actualquiz()
        elif questions[0] == 'Q1':
            print("Question 2 Has been Selected")
            del questions[0]
            questiontot += 1
            quizmenu = Toplevel(menu)
            quizmenu.title("Quiz")
            quizmenu.geometry("512x512")
            test_entry = Entry(quizmenu, show="", textvariable = test123)
            test_entry.pack()
            Button(quizmenu, text = "Quit").pack()
   #         test_info = test123.get()
   #         if test_info == 0:
   #             print("wtf")
   #         else:
   #             print("how is this working")
            print("XDLMAO2")
            time.sleep(1)
            break
            time.sleep(1)
            actualquiz()
        elif questions[0] == 'Q2':
            print("Question 3 Has been Selected")
            del questions[0]
            questiontot += 1
            quizmenu = Toplevel(menu)
            quizmenu.title("Quiz")
            quizmenu.geometry("512x512")
            test_entry = Entry(quizmenu, show="", textvariable = test123)
            test_entry.pack()
            Button(quizmenu, text = "Quit").pack()
    #        test_info = test123.get()
    #       if test_info == 0:
    #            print("wtf")
    #        else:
    #            print("how is this working")
            print("XDLMAO3")
            time.sleep(1)
            break
            time.sleep(1)
            actualquiz()
        elif questions[0] == 'Q3':
            print("Question 4 Has been Selected")
            del questions[0]
            questiontot += 1
            quizmenu = Toplevel(menu)
            quizmenu.title("Quiz")
            quizmenu.geometry("512x512")
            test_entry = Entry(quizmenu, show="", textvariable = test123)
            test_entry.pack()
            Button(quizmenu, text = "Quit").pack()
    #        test_info = test123.get()
    #        if test_info == 0:
    #            print("wtf")
    #        else:
    #            print("how is this working")
            
            print("XDLMAO4")
            time.sleep(1)
            break
            time.sleep(1)
            actualquiz()


    if questiontot < 4:
        quizmenu.destroy
        actualquiz()
    else:
        print("im happy")

                                

                                
                        
       







def session():
    global sessionmenu
    sessionmenu = Toplevel(menu)
    sessionmenu.title("Quiz")
    sessionmenu.geometry("512x512")
    Label(sessionmenu, text = "Welcome to the Quiz").pack()
    Button(sessionmenu, text = "Start", command =actualquiz).pack()
    Button(sessionmenu, text = "Scores").pack()
    Button(sessionmenu, text = "Quit", command =killsessionmenu).pack()
                         


def login_correct():
    session()

def login_wrong():
    global wrongmenu
    wrongmenu = Toplevel(menu)
    wrongmenu.title("Wrong")
    wrongmenu.geometry("200x150")
    Label(wrongmenu, text = "Wrong Password").pack()
    Button(wrongmenu, width = 300, height = 10, text ="OK", command =killwrongmenu).pack()


def login_failed():
    global failedmenu
    failedmenu = Toplevel(menu)
    failedmenu.title("Failed")
    failedmenu.geometry("200x150")
    Label(failedmenu, text = "Username not found").pack()
    Button(failedmenu, width = 300, height = 10, text ="OK", command =killfailedmenu).pack()



def reguser():

    print("Someone is making an account")
    
    username_info = username.get()
    password_info = password.get()

    file=open(username_info, "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(regmenu, text = "Registration Complete", fg = "green" ,font = ("calibri", 12)).pack()


def login_verify():

    usernamev = username_check.get()
    passwordv = password_check.get()
    username_entry2.delete(0, END)
    password_entry2.delete(0, END)
    
    listoffiles = os.listdir()
    if usernamev in listoffiles:
        file1 = open(usernamev, "r")
        verify = file1.read().splitlines()
        if passwordv in verify:
            print("Welcome")
            login_correct()
        else:
            print("Wrong password")
            login_wrong()

    else:
        print("Go create a account")
        login_failed()
        


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
    Label(regmenu, text = "Username").pack()
    username_entry = Entry(regmenu, textvariable = username)
    username_entry.pack()
    Label(regmenu, text = "Password").pack()
    password_entry = Entry(regmenu, show="*", textvariable = password)
    password_entry.pack()
    Label(regmenu, text = "").pack()
    Button(regmenu, command = reguser, text = "Register", width = 15, height = 2).pack()
    Label(regmenu, text = "").pack()
    Button(regmenu, text = "Back", width = 15, command = killregmenu, height = 2).pack()

def login(): #all your passwords are in plain text , facebook was my inspiration
    print("someone is trying to guess a password")
    global logmenu
    logmenu = Toplevel(menu)
    logmenu.title("Login")
    logmenu.geometry("350x300")
    Label(logmenu, text = "Login").pack()
    Label(logmenu, text = "").pack()


    global username_check
    global password_check

    
    username_check = StringVar()
    password_check = StringVar()

    global username_entry2
    global password_entry2
    
    Label(logmenu, text = "Username").pack()
    username_entry2 = Entry(logmenu, textvariable = username_check)
    username_entry2.pack()
    Label(logmenu, text = "Password").pack()
    password_entry2 = Entry(logmenu, show="*", textvariable = password_check)
    password_entry2.pack()
    Label(logmenu, text = "").pack()
    Button(logmenu, text = "Login", width = 15, command = login_verify, height = 2).pack()
    Label(logmenu, text = "").pack()
    Button(logmenu, text = "Back", width = 15, command = killloginmenu, height = 2).pack()







def login_menu():    #Basically the login system ui
    global menu      #Globalising it so I can use it anywhere




    menu = Tk()                                                                                                 #Start login gui
    menu.geometry("350x300")                                                                                    #Window size
    menu.title("Python Music Quiz")                                                                             #Title
    Label(text = "Python Music Quiz", bg = "grey", width = "350", height = "4", font = ("Calibri", 13)).pack()  #Fancy title text
    Label(text = "").pack()                                                                                     #Blank Spacer 900000000                                     
    Button(text = "Login", command = login, height = "4", width = "40").pack()                                  #Directs to login function
    Label(text = "").pack()                                                                                     #Blank Spacer 900000000
    Button(text = "Register", command = register, height = "4", width = "40").pack()                            #Directs to register function


    menu.mainloop()                                                                                             #Loops it untill it reciveces a input
    
login_menu()                                                                                                    #Starts the login_menu()
