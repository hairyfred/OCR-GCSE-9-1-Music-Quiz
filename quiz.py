#####Expect tons of spaghetti code , plus i doubt you even read this
#####Just copy and paste it into google to see if i copy and pasted

# All needed modules here d
from tkinter import *
import os
import random
import time
import base64
import csv


songname = 1
album = 2
art = 3
choice1 = 4
choice2 = 5
choice3 = 6
img = 0
status = 0


class quizarray:
    def __init__(change):
        change.question = '1'
        change.song_name = 'default'
        change.awnser1 = '1'
        change.artist = '1'
        change.art = '1'
        change.score = 1


user = quizarray()

quizquestion = {
    '1': {
        songname: "Do I Wanna Know",
        album: "arctic monkeys",
        art: "q1.gif",
        choice1: "R U Mine?",
        choice2: "Do I Wanna know?",
        choice3: "Fluorescent Adolescent"
    },
    
    '2': {
        songname: "Through the Fire and the Flames",
        album: "inhuman rampage",
        art: "q2.gif",
        choice1: "Guitar Hero 3 OST",
        choice2: "Fire and Flames",
        choice3: "Through the Fire and the Flames"
    },
    
    '3': {
        songname: "Sweden",
        album: "minecraft",
        art: "q3.gif",
        choice1: "Sweden",
        choice2: "Far",
        choice3: "Cat"
    },
    
    '4': {
        songname: "The Four Horsemen",
        album: "metallica",
        art: "q4.gif",
        choice1: "Enter Sandman",
        choice2: "The Four Horsemen",
        choice3: "Fuel"
    }
}


quizquestionbackup = {
    '1': {
        songname: "do i wanna know",
        album: "arctic monkeys",
        art: "q1.gif",
        choice1: "R U Mine?",
        choice2: "Do I wanna know?",
        choice3: "Fluorescent Adolescent"
    },
    
    '2': {
        songname: "through the fire and the flames",
        album: "inhuman rampage",
        art: "q2.gif",
        choice1: "Guitar Hero 3 OST",
        choice2: "Fire and Flames",
        choice3: "Through the Fire and the Flames"
    },
    
    '3': {
        songname: "sweden",
        album: "minecraft",
        art: "q3.gif",
        choice1: "Sweden",
        choice2: "Far",
        choice3: "Cat"
    },
    
    '4': {
        songname: "The Four Horsemen",
        album: "metallica",
        art: "q4.gif",
        choice1: "Enter Sandman",
        choice2: "The Four Horsemen",
        choice3: "Fuel"
    }
}

print(quizquestion[str(user.question)])
questiontot = 0
endme = 1

listoffiles = os.listdir()
# Legit its a tkinter massacare in this section
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


def killcorrectmenu():
    correctmenu.destroy()


def killmenu():
    menu.destroy()


def killsession():
    sessionmenu.destroy()

def killaccountexists():
    accountexists1.destroy()

def killaccountmade():
    accountmade1.destroy()

def killaddpassword():
    addpassword1.destroy()

# rip

test123 = 1

a = True


def login_menu():  # Basically the login system ui
    global menu  # Globalising it so I can use it anywhere

    menu = Tk()  # Start login gui
    menu.geometry("350x300")  # Window size
    menu.title("Python Music Quiz")  # Title
    Label(text="Python Music Quiz", bg="grey", width="350", height="3",
          font=("Gill Sans Ultra Bold", 15)).pack()  # Fancy title text
    Label(text="").pack()  # Blank Spacer 900000000
    Button(text="Login", command=login, height="3", width="40").pack()  # Directs to login function
    Label(text="").pack()  # Blank Spacer 900000000
    Button(text="Register", command=register, height="3", width="40").pack()  # Directs to register function

    menu.mainloop()


def login():  # all your passwords are in plain text , facebook was my inspiration
    print(
        "someone is trying to guess a password")  # Prints in console , good for error testing so I know when somthing fails
    global logmenu  # So I can use it anywhere
    logmenu = Toplevel(menu)  # Brings current window to front
    logmenu.title("Login")
    logmenu.geometry("350x300")
    Label(logmenu, text="Login").pack()  # Submits data
    Label(logmenu, text="").pack()

    global username_check  # Allows me to use it anywhere
    global password_check

    username_check = StringVar()  # Converts it into strings to prevent
    password_check = StringVar()  # errors if the password is a number

    global username_entry2
    global password_entry2

    Label(logmenu, text="Username").pack()
    username_entry2 = Entry(logmenu, textvariable=username_check)
    username_entry2.pack()
    Label(logmenu, text="Password").pack()
    password_entry2 = Entry(logmenu, show="*", textvariable=password_check)  # Sumbits data to other function
    password_entry2.pack()
    Label(logmenu, text="").pack()
    Button(logmenu, text="Login", width=15, command=login_verify, height=2).pack()
    Label(logmenu, text="").pack()
    Button(logmenu, text="Back", width=15, command=killloginmenu, height=2).pack()


def register():  # all the account data handling , plz send help
    global regmenu
    regmenu = Toplevel(menu)
    regmenu.title("Register")
    regmenu.geometry("350x300")

    global username
    global password
    global username_entry
    global password_entry
    global status1
    username = StringVar()
    password = StringVar()

    Label(regmenu, text="Registeration").pack()
    Label(regmenu, text="").pack()
    Label(regmenu, text="Username").pack()
    username_entry = Entry(regmenu, textvariable=username)
    username_entry.pack()
    Label(regmenu, text="Password").pack()
    password_entry = Entry(regmenu, show="*", textvariable=password)
    password_entry.pack()
    Label(regmenu, text="").pack()
    status1 = 0
    Button(regmenu, command=reguser, text="Register", width=15, height=2).pack()
    Label(regmenu, text="").pack()
    Button(regmenu, text="Back", width=15, command=killregmenu, height=2).pack()

def statusstuff():
    status1 + 1
def reguser():
    print("Someone is making an account")
    global status
    global status1

    status2 = 1
    status = 0
    username_info = username.get()
    password_info = password.get()# Gets entered Username
    if username_info in listoffiles:
        accountexists()
    else:
        if password_info == "":
            addpassword()

        else:
                                    # Gets entered Password
            random.seed(password_info, 2)
            hashpassword = random.random()
            hashpasswordtext = str(hashpassword)
            print(hashpassword)
            file = open(username_info, "w")  # Makes a new file named after username
            file.write(username_info + "\n")  # Writes Username
            file.write(hashpasswordtext)  # Writes password
            file.close()  # Closes the file

            username_entry.delete(0, END)
            password_entry.delete(0, END)  # Resets line
            accountmade()

def addpassword():
    global addpassword1
    addpassword1 = Toplevel(menu)
    addpassword1.title("")
    addpassword1.geometry("200x150")
    Label(addpassword1, text="Add a Password").pack()
    Button(addpassword1, width=300, height=10, text="OK", command=killaddpassword).pack()

def accountexists():  # Wrong password
    global accountexists1
    accountexists1 = Toplevel(menu)
    accountexists1.title("")
    accountexists1.geometry("200x150")
    Label(accountexists1, text="Account Exists").pack()
    Button(accountexists1, width=300, height=10, text="OK", command=killaccountexists).pack()

def accountmade():
    global accountmade1
    accountmade1 = Toplevel(menu)
    accountmade1.title("")
    accountmade1.geometry("200x150")
    Label(accountmade1, text="Registration Complete", fg="green", font=("calibri", 12)).pack()
    Button(accountmade1, width=300, height=10, text="OK", command=killaccountmade).pack()

def big_pass():
    number = 420.;
    num2 = 0;
    while (num2 < 1000):
        number = number * 2
        num2 = num2 + 1
    return number


def login_verify():  # Verifys details

    usernamev = username_check.get()
    passwordv = password_check.get()
    username_entry2.delete(0, END)
    password_entry2.delete(0, END)

    random.seed(passwordv, 2)
    hashpasswordlogin = random.random()
    hashpasswordtextlogin = str(hashpasswordlogin)
    print(hashpasswordlogin)
    listoffiles = os.listdir()  # Lists files in its current directory
    if usernamev in listoffiles:
        file1 = open(usernamev, "r")  # Reads them only! not wipes them
        verify = file1.read().splitlines()  # Splits the lines due to username and password being on differnt lines
        if hashpasswordtextlogin in verify:
            print("Welcome")
            login_correct()  # Brings up a confirmation Screen
        else:
            print("Wrong password")
            login_wrong()  # Brings up a failure screen

    else:
        print("Go create a account")
        login_failed()


def login_failed():  # For invalid usernames
    global failedmenu
    failedmenu = Toplevel(menu)
    failedmenu.title("Failed")
    failedmenu.geometry("200x150")
    Label(failedmenu, text="Username not found").pack()
    Button(failedmenu, width=300, height=10, text="OK", command=killfailedmenu).pack()  # Puts you back to login screen


def login_wrong():  # Wrong password
    global wrongmenu
    wrongmenu = Toplevel(menu)
    wrongmenu.title("Wrong")
    wrongmenu.geometry("200x150")
    Label(wrongmenu, text="Wrong Password").pack()
    Button(wrongmenu, width=300, height=10, text="OK", command=killwrongmenu).pack()


def login_correct():  # Wrong password
    global correctmenu
    correctmenu = Toplevel(menu)
    correctmenu.title("Correct")
    correctmenu.geometry("200x150")
    Label(correctmenu, text="Welcome").pack()
    Button(correctmenu, width=300, height=10, text="OK", command=session).pack()


def session():  # Actual quiz after logged in
    killcorrectmenu()  # Kills the login menu
    killloginmenu()
    global sessionmenu
    sessionmenu = Toplevel(menu)
    sessionmenu.title("Quiz")
    sessionmenu.geometry("512x512")
    Label(sessionmenu, bg="grey", width="350", height="3", font=("Gill Sans Ultra Bold", 25),
          text="Welcome to the Quiz").pack()  # New Menu for quiz options
    Label(sessionmenu, text="").pack()
    Button(sessionmenu, width=50, height=3, text="Start", command=actualquiz).pack()
    Label(sessionmenu, text="").pack()
    Button(sessionmenu, width=50, height=3, text="Scores").pack()
    Label(sessionmenu, text="").pack()
    Button(sessionmenu, width=50, height=3, text="Quit", command=killsession).pack()
    Label(sessionmenu, text="").pack()
    photo = PhotoImage(file="passion.gif")
    Label(sessionmenu, image=photo).pack()
    Label.image = photo



def ultimateback():  # NOT USED FOR NOW UNTIL FIXED
    killsessionmenu #probs will never be used but ill probs forget about it cause my code is more of a mess than brexit
    login_menu()

questionamount = 0







def actualquiz():
    user.score = 0



    def showNewQuestion(questionamount):
        if questionamount > 3:
            print("finish")
            quizquestion.update(quizquestionbackup)
            return
        global randomquestion

        randomquestion = random.choice(list(quizquestion.keys()))
        print(randomquestion)
        user.question = randomquestion
        print(user.question)
        label = Label()
        global quiz
        quiz = Toplevel(menu)
        quiz.title("Quiz")
        quiz.geometry("512x512")
        Label(quiz, text="").pack()
        img = PhotoImage(file=quizquestion[str(user.question)][art])
        Label(quiz, image=img).pack()
        label.image = img

        Label(quiz, text="Whats the name of this song?", font=("arial", 25), height=1).pack()
        Label(quiz, text="").pack()

        def newquiz():

            quiznext.destroy()
            del quizquestion[str(user.question)]
            showNewQuestion(questionamount + 1)

        def nextquestion():
            quiz.destroy()
            global quiznext
            quiznext = Toplevel(menu)
            quiznext.title("Next")

            quiznext.geometry("200x150")

            Label(quiznext, text="").pack()
            Label(quiznext, font=("arial", 18), text="Next Question?").pack()
            Label(quiznext, text="").pack()
            Button(quiznext, font=("arial", 18), width=10, text="OK", command=newquiz).pack()

        def awnsercheck():
            user.song_name = quizquestion[str(user.question)][songname]
            print(user.awnser1)
            if user.awnser1 == user.song_name:
                user.score = user.score + 1
                print("point added")
                print(user.score)
                nextquestion()
            else:
                nextquestion()


        def choice1select():
            user.awnser1 = quizquestion[str(user.question)][choice1]
            awnsercheck()

        Button(quiz, font=("arial", 18), width=30, text=quizquestion[str(user.question)][choice1], command=choice1select).pack()
        Label(quiz, text="").pack()
        def choice2select():
            user.awnser1 = quizquestion[str(user.question)][choice2]
            awnsercheck()

        Button(quiz, font=("arial", 18), width=30,  text=quizquestion[str(user.question)][choice2], command=choice2select).pack()
        Label(quiz, text="").pack()
        def choice3select():
            user.awnser1 = quizquestion[str(user.question)][choice3]
            awnsercheck()

        Button(quiz, font=("arial", 18), width=30, text=quizquestion[str(user.question)][choice3], command=choice3select).pack()
        Label(quiz, text="").pack()








    showNewQuestion(questionamount)

login_menu()

