#####Expect tons of spaghetti code , plus i doubt you even read this
#####Just copy and paste it into google to see if i copy and pasted

# All needed modules here d
from tkinter import *
import os
import random
import time
import base64
import winsound
import csv
import pickle


#with open('info.txt', 'rb') as handle:
 # b = pickle.loads(handle.read())
#print(b[str(user.question)][choice1])

sanitycheck = 1
songname = 1
album = 2
art = 3
choice1 = 4
choice2 = 5
choice3 = 6
img = 0
status = 0
active = 0
wav = 0
largefont = ('Verdana', 25)


class quizarray:
    def __init__(change):
        change.question = '1'
        change.song_name = 'default'
        change.awnser1 = '1'
        change.artist = '1'
        change.art = '1'
        change.wav = 1
        change.score = 0
        change.quizactive = 0
        change.loginactive = 0
        change.regactive = 0
        change.questionscore = 0


user = quizarray()


quizquestion = pickle.load(open("info.p", "rb"))

quizquestionbackup = pickle.load(open("infobackup.p", "rb"))


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
    user.loginactive = 0
    logmenu.destroy()


def killregmenu():
    user.regactive = 0
    regmenu.destroy()


def killquestion():
    quizmenu.destroy()


def killcorrectmenu():
    correctmenu.destroy()


def killmenu():
    menu.destroy()


def killsession():
    sessionmenu.destroy()
    user.loginactive = 0


def killaccountexists():
    accountexists1.destroy()


def killaccountmade():
    accountmade1.destroy()


def killaddpassword():
    addpassword1.destroy()


def killquiztryagain():
    quiztryagain.destroy()


# rip

test123 = 1

a = True


def login_menu():  # Basically the login system ui

    global menu  # Globalising it so I can use it anywhere

    menu = Tk()  # Start login gui
    menu.attributes("-fullscreen", True)
    menu.geometry("350x300")  # Window size
    Label(text="", height="9").pack()

    menu.title("Python Music Quiz")  # Title
    Label(text="Python Music Quiz", bg="grey", width="350", height="3",
          font=("Gill Sans Ultra Bold", 40)).pack()  # Fancy title text
    Label(text="").pack()  # Blank Spacer 900000000
    Button(text="Login", command=loginactivefix, height="6", width="80").pack()  # Directs to login function
    Label(text="").pack()  # Blank Spacer 900000000
    Button(text="Register", command=regactivecheck, height="6", width="80").pack()  # Directs to register function
    Label(text="").pack()
    Button(text="Quit", command=quit, height="6", width="80").pack()

    menu.mainloop()


def loginactivefix():
    if user.loginactive == 0:
        login()
    else:
        print("")


def login():  # all your passwords are in plain text , facebook was my inspiration
    user.loginactive = 1
    print(
        "someone is trying to guess a password")  # Prints in console , good for error testing so I know when somthing fails
    global logmenu  # So I can use it anywhere
    logmenu = Toplevel(menu)  # Brings current window to front
    logmenu.attributes("-fullscreen", True)
    logmenu.overrideredirect(True)

    logmenu.title("Login")
    logmenu.geometry("350x300")
    Label(logmenu, text="Login", bg="grey", width="350", height="3",
          font=("Gill Sans Ultra Bold", 40)).pack()  # Submits data
    Label(logmenu, text="").pack()

    global username_check  # Allows me to use it anywhere
    global password_check

    username_check = StringVar()  # Converts it into strings to prevent
    password_check = StringVar()  # errors if the password is a number

    global username_entry2
    global password_entry2

    Label(logmenu, text="Username", height="2", font=largefont).pack()
    username_entry2 = Entry(logmenu, textvariable=username_check, font=largefont)
    username_entry2.pack()
    Label(logmenu, text="Password", height="2", font=largefont).pack()
    password_entry2 = Entry(logmenu, show="*", textvariable=password_check,
                            font=largefont)  # Sumbits data to other function
    password_entry2.pack()
    Label(logmenu, text="").pack()
    Button(logmenu, text="Login", command=login_verify, height="6", width="80").pack()
    Label(logmenu, text="").pack()
    Button(logmenu, text="Back", command=killloginmenu, height="6", width="80").pack()


def regactivecheck():
    if user.regactive == 0:
        user.regactive = 1
        register()
    else:
        print("")


def register():  # all the account data handling , plz send help
    print(user.regactive)
    global regmenu
    regmenu = Toplevel(menu)
    regmenu.attributes("-fullscreen", True)
    regmenu.overrideredirect(True)
    regmenu.title("Register")
    regmenu.geometry("350x300")

    global username
    global password
    global username_entry
    global password_entry
    global status1
    username = StringVar()
    password = StringVar()

    Label(regmenu, text="Registeration", bg="grey", width="350", height="3",
          font=("Gill Sans Ultra Bold", 40)).pack()
    Label(regmenu, text="").pack()
    Label(regmenu, text="Username", height="2", font=largefont).pack()
    username_entry = Entry(regmenu, textvariable=username, font=largefont)
    username_entry.pack()
    Label(regmenu, text="Password", height="2", font=largefont).pack()
    password_entry = Entry(regmenu, show="*", textvariable=password, font=largefont)
    password_entry.pack()
    Label(regmenu, text="").pack()
    status1 = 0
    Button(regmenu, command=reguser, text="Register", height="6", width="80").pack()
    Label(regmenu, text="").pack()
    Button(regmenu, text="Back", command=killregmenu, height="6", width="80").pack()


def statusstuff():
    status1 + 1


def reguser():
    print("Someone is making an account")
    global status
    global status1

    status2 = 1
    status = 0
    username_info = username.get()
    password_info = password.get()  # Gets entered Username
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
    addpassword1.attributes("-fullscreen", True)
    addpassword1.title("")
    addpassword1.geometry("200x150")
    Label(addpassword1, text="Add a Password").pack()
    Button(addpassword1, width=300, height=10, text="OK", command=killaddpassword).pack()


def accountexists():  # Wrong password
    global accountexists1
    accountexists1 = Toplevel(menu)
    accountexists1.attributes("-fullscreen", True)
    accountexists1.title("")
    accountexists1.geometry("200x150")
    Label(accountexists1, text="Account Exists").pack()
    Button(accountexists1, width=300, height=10, text="OK", command=killaccountexists).pack()


def accountmade():
    global accountmade1
    accountmade1 = Toplevel(menu)
    accountmade1.attributes("-fullscreen", True)
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
    failedmenu.attributes("-fullscreen", True)
    failedmenu.title("Failed")
    failedmenu.geometry("200x150")
    Label(failedmenu, text="Username not found").pack()
    Button(failedmenu, width=300, height=10, text="OK", command=killfailedmenu).pack()  # Puts you back to login screen


def login_wrong():  # Wrong password
    global wrongmenu
    wrongmenu = Toplevel(menu)
    wrongmenu.attributes("-fullscreen", True)
    wrongmenu.title("Wrong")
    wrongmenu.geometry("200x150")
    Label(wrongmenu, text="Wrong Password").pack()
    Button(wrongmenu, width=300, height=10, text="OK", command=killwrongmenu).pack()


def login_correct():  # Wrong password
    global correctmenu
    correctmenu = Toplevel(menu)
    correctmenu.attributes("-fullscreen", True)
    correctmenu.title("Correct")
    correctmenu.geometry("200x150")
    Label(correctmenu, text="Welcome").pack()
    user.loginactive = 1
    Button(correctmenu, width=300, height=10, text="OK", command=session).pack()


def session():  # Actual quiz after logged in
    killcorrectmenu()  # Kills the login menu
    killloginmenu()
    global sessionmenu
    sessionmenu = Toplevel(menu)
    sessionmenu.attributes("-fullscreen", True)
    sessionmenu.title("Quiz")
    sessionmenu.geometry("512x512")
    Label(sessionmenu, bg="grey", width="350", height="3", font=("Gill Sans Ultra Bold", 25),
          text="Welcome to the Quiz").pack()  # New Menu for quiz options
    Label(sessionmenu, text="").pack()
    Button(sessionmenu, width=50, height=3, text="Start", command=actualquizdupefix).pack()
    Label(sessionmenu, text="").pack()
    Button(sessionmenu, width=50, height=3, text="Scores").pack()
    Label(sessionmenu, text="").pack()
    Button(sessionmenu, width=50, height=3, text="Quit", command=killsession).pack()
    Label(sessionmenu, text="").pack()
    photo = PhotoImage(file="passion.gif")
    Label(sessionmenu, image=photo).pack()
    Label.image = photo


def ultimateback():  # NOT USED FOR NOW UNTIL FIXED
    killsessionmenu  # probs will never be used but ill probs forget about it cause my code is more of a mess than brexit
    login_menu()


questionamount = 0


def actualquizdupefix():
    if user.quizactive == 0:  # Stops multiple quiz's being opened at once
        actualquiz()
    else:
        print("")


def actualquiz():
    user.quizactive = 1  # To prevent duplicate quiz sessions

    def finalscorepage():
        user.questionscore = 0
        global finalscore
        finalscore = Toplevel(menu)
        finalscore.attributes("-fullscreen", True)
        finalscore.title("Final Score!")  # Final score display page
        finalscore.geometry("512x512")
        Label(finalscore, text="", height="12").pack()
        Label(finalscore, text="You scored", font=("arial", 50), height=3).pack()
        Label(finalscore, text=(user.score), font=("arial", 50), height=3).pack()

    def showNewQuestion(questionamount):
        if questionamount > 3:  # Counts question left
            print(user.score, "is the final score")
            print("finish")
            user.active = 0  # Resets the quiz session active check
            quizquestion.update(quizquestionbackup)  # Resets the quiz questions
            finalscorepage()  # Opens final score page
        else:
            global randomquestion
            user.questionscore = 0
            randomquestion = random.choice(
                list(quizquestion.keys()))  # Counts the questions , makes it easier later on to add questions
            print(randomquestion)
            user.question = randomquestion  # Assigns the value to a class
            print(user.question)
            label = Label()
            global quiz
            quiz = Toplevel(menu)
            quiz.attributes("-fullscreen", True)
            quiz.title("Quiz")
            quiz.geometry("512x512")
            Label(quiz, text="").pack()
            img = PhotoImage(file=quizquestion[str(user.question)][art])  # Looks in the dictornary for the right img
            Label(quiz, image=img).pack()
            label.image = img
            user.wav = (quizquestion[str(user.question)][wav])
            winsound.PlaySound(user.wav, winsound.SND_ASYNC)
            Label(quiz, text="Whats the name of this song?", font=("arial", 25), height=1).pack()
            Label(quiz, text="").pack()

        def newquiz():

            quiznext.destroy()
            del quizquestion[str(user.question)]  # After the question is used it removes it so it cant be repeated
            showNewQuestion(questionamount + 1)  # Says 1 more question has been completed

        def nextquestion():

            quiz.destroy()
            global quiznext
            quiznext = Toplevel(menu)
            quiznext.attributes("-fullscreen", True)
            quiznext.title("Next")
            winsound.PlaySound(None, winsound.SND_PURGE)

            quiznext.geometry("200x150")

            Label(quiznext, text="").pack()
            Label(quiznext, font=("arial", 18), text="Next Question?").pack()
            Label(quiznext, text="").pack()
            Label(quiznext, text=(user.score)).pack()
            Label(quiznext, text=(user.questionscore)).pack()
            user.questionscore = 0
            Button(quiznext, font=("arial", 18), width=10, text="OK", command=newquiz).pack()

        def awnsercheck():
            print(user.score)
            user.song_name = quizquestion[str(user.question)][songname]  # Gets the song from the dictionary


            if user.awnser1 == user.song_name:  # Checks if its the right song
                if user.questionscore == 1:

                    user.score = user.score + 3

            if user.awnser1 == user.song_name: #Checks if its the right song
                if user.questionscore == 1: #Checks if the user has
                        
                    user.score = user.score + 3 #Gives 3 score for people who awnser first try

                    nextquestion()

                elif user.questionscore == 2:

                    user.score = user.score + 1  # adds a point if its the right question

                    user.score = user.score + 1#adds a point if its the right question but took 2 trys


                    print("point added")
                    print(user.score)
                    nextquestion() #they failed 3 times so no points :(
            elif user.questionscore == 2:
                nextquestion()

            else:
                tryagain()
                


        def tryagain(): #Because I relised at the last second you needed multiple trys
            

            global quiztryagain
            quiztryagain = Toplevel(menu)
            quiztryagain.attributes("-fullscreen", True)
            quiztryagain.title("Try Again")
            winsound.PlaySound(None, winsound.SND_PURGE)

            quiztryagain.geometry("200x150")

            Label(quiztryagain, text="").pack()
            Label(quiztryagain, font=("arial", 18), text="Try Again!").pack()
            Label(quiztryagain, text="").pack()
            Label(quiztryagain, text=(user.score))
            Button(quiztryagain, font=("arial", 18), width=10, text="OK", command=killquiztryagain).pack()
            print(user.questionscore)

        def choice1select():
            user.questionscore = user.questionscore + 1
            user.awnser1 = quizquestion[str(user.question)][choice1]
            awnsercheck()

        Button(quiz, font=("arial", 18), width=30, text=quizquestion[str(user.question)][choice1],
               command=choice1select).pack()
        Label(quiz, text="").pack()

        def choice2select():
            user.questionscore = user.questionscore + 1
            user.awnser1 = quizquestion[str(user.question)][choice2]  # Assigns the button the right song
            awnsercheck()

        Button(quiz, font=("arial", 18), width=30, text=quizquestion[str(user.question)][choice2],
               command=choice2select).pack()
        Label(quiz, text="").pack()

        def choice3select():
            user.questionscore = user.questionscore + 1
            user.awnser1 = quizquestion[str(user.question)][choice3]
            awnsercheck()

        Button(quiz, font=("arial", 18), width=30, text=quizquestion[str(user.question)][choice3],
               command=choice3select).pack()
        Label(quiz, text="").pack()

    showNewQuestion(questionamount)


login_menu()
