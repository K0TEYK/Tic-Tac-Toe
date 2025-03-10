from tkinter import *
from tkinter import messagebox as mb
import random

game = Tk()
game.title("Tic Tac Toe")

game.geometry("")

app = Frame(game)
app.grid()

XO = [[0,0,0], [0,0,0], [0,0,0]]
def win():
    if((XO[0][0] == 1 and XO[1][0] == 1 and XO[2][0] == 1) or 
       (XO[0][1] == 1 and XO[1][1] == 1 and XO[2][1] == 1) or 
       (XO[0][2] == 1 and XO[1][2] == 1 and XO[2][2] == 1) or
       (XO[0][0] == 1 and XO[0][1] == 1 and XO[0][2] == 1) or 
       (XO[1][0] == 1 and XO[1][1] == 1 and XO[1][2] == 1) or
       (XO[2][0] == 1 and XO[2][1] == 1 and XO[2][2] == 1) or 
       (XO[0][0] == 1 and XO[1][1] == 1 and XO[2][2] == 1) or 
       (XO[0][2] == 1 and XO[1][1] == 1 and XO[2][0] == 1)) :
        mb.showinfo('Congratulation', 'Переміг Х')
        game.destroy()
    elif((XO[0][0] == 2 and XO[1][0] == 2 and XO[2][0] == 2) or 
       (XO[0][1] == 2 and XO[1][1] == 2 and XO[2][1] == 2) or 
       (XO[0][2] == 2 and XO[1][2] == 2 and XO[2][2] == 2) or
       (XO[0][0] == 2 and XO[0][1] == 2 and XO[0][2] == 2) or 
       (XO[1][0] == 2 and XO[1][1] == 2 and XO[1][2] == 2) or
       (XO[2][0] == 2 and XO[2][1] == 2 and XO[2][2] == 2) or 
       (XO[0][0] == 2 and XO[1][1] == 2 and XO[2][2] == 2) or 
       (XO[0][2] == 2 and XO[1][1] == 2 and XO[2][0] == 2)):
        mb.showinfo('Congratulation', 'Переміг О')
        game.destroy()
    elif(XO[0][0] != 0 and XO[1][0] != 0 and XO[2][0] != 0 and
         XO[0][1] != 0 and XO[1][1] != 0 and XO[2][1] != 0 and
         XO[0][2] != 0 and XO[1][2] != 0 and XO[2][2] != 0 and
         XO[0][0] != 0 and XO[0][1] != 0 and XO[0][2] != 0 and 
         XO[1][0] != 0 and XO[1][1] != 0 and XO[1][2] != 0 and
         XO[2][0] != 0 and XO[2][1] != 0 and XO[2][2] != 0 and 
         XO[0][0] != 0 and XO[1][1] != 0 and XO[2][2] != 0 and
         XO[0][2] != 0 and XO[1][1] != 0 and XO[2][0] != 0):
        mb.showinfo('Wow', 'Нічия')
        game.destroy()

player = "X"
def change_player():
    global player

    if player == 'X':
        player = 'O'
    else:
        player = 'X'
    Player['text'] = "Зараз ходить " + player

def tl():
    if topLeft['text'] == '':
        if player == 'X':
            XO[0][0] = 1
        else:
            XO[0][0] = 2
        topLeft.configure(text = player)
        change_player()
        win()
    else:
        mb.showerror('Шахрай', 'Ви не можете змінювати поставлений знак') 


def tm():
    if topMid['text'] == '':
        if player == 'X':
            XO[0][1] = 1
        else:
            XO[0][1] = 2
        topMid.configure(text = player)
        change_player()
        win()
    else:
        mb.showerror('Шахрай', 'Ви не можете змінювати поставлений знак') 


def tr():
    if topRight['text'] == '': 
        if player == 'X':
            XO[0][2] = 1
        else:
            XO[0][2] = 2
        topRight.configure(text = player)
        change_player()
        win()
    else:
        mb.showerror('Шахрай', 'Ви не можете змінювати поставлений знак') 


def ml():
    if midLeft['text'] == '':
        if player == 'X':
            XO[1][0] = 1
        else:
            XO[1][0] = 2
        midLeft.configure(text = player)
        change_player()
        win()
    else:
        mb.showerror('Шахрай', 'Ви не можете змінювати поставлений знак') 


def mm():
    if midMid['text'] == '': 
        if player == 'X':
            XO[1][1] = 1
        else:
            XO[1][1] = 2
        midMid.configure(text = player)
        change_player()
        win()
    else:
        mb.showerror('Шахрай', 'Ви не можете змінювати поставлений знак') 


def mr():
    if midRight['text'] == '': 
        if player == 'X':
            XO[1][2] = 1
        else:
            XO[1][2] = 2
        midRight.configure(text = player)
        change_player()
        win()
    else:
        mb.showerror('Шахрай', 'Ви не можете змінювати поставлений знак') 


def bl():
    if botLeft['text'] == '':
        if player == 'X':
            XO[2][0] = 1
        else:
            XO[2][0] = 2
        botLeft.configure(text = player)
        change_player()
        win()
    else:
        mb.showerror('Шахрай', 'Ви не можете змінювати поставлений знак') 


def bm():
    if botMid['text'] == '': 
        if player == 'X':
            XO[2][1] = 1
        else:
            XO[2][1] = 2
        botMid.configure(text = player)
        change_player()
        win()
    else:
        mb.showerror('Шахрай', 'Ви не можете змінювати поставлений знак') 


def br():
    if botRight['text'] == '':
        if player == 'X':
            XO[2][2] = 1
        else:
            XO[2][2] = 2
        botRight.configure(text = player)
        change_player()
        win()
    else:
        mb.showerror('Шахрай', 'Ви не можете змінювати поставлений знак') 



topLeft = Button(app, text = "", activebackground="red", command=tl)
topLeft.grid(row = 0, column = 0, ipadx=20, ipady=18, padx=10, pady=10)

topMid = Button(app, text = "", activebackground="red", command=tm)
topMid.grid(row = 0, column = 1, ipadx=20, ipady=18, padx=10, pady=10)

topRight = Button(app, text = "", activebackground="red", command=tr)
topRight.grid(row = 0, column = 2, ipadx=20, ipady=18, padx=10, pady=10)

midLeft = Button(app, text = "", activebackground="red", command=ml)
midLeft.grid(row = 1, column = 0, ipadx=20, ipady=18, padx=10, pady=10)

midMid = Button(app, text = "", activebackground="red", command=mm)
midMid.grid(row = 1, column = 1, ipadx=20, ipady=18, padx=10, pady=10)

midRight = Button(app, text = "", activebackground="red", command=mr)
midRight.grid(row = 1, column = 2, ipadx=20, ipady=18, padx=10, pady=10)


botLeft = Button(app, text = "", activebackground="red", command=bl)
botLeft.grid(row = 2, column = 0, ipadx=20, ipady=18, padx=10, pady=10)

botMid = Button(app, text = "", activebackground="red", command=bm)
botMid.grid(row = 2, column = 1, ipadx=20, ipady=18, padx=10, pady=10)

botRight = Button(app, text = "", activebackground="red", command=br)
botRight.grid(row = 2, column = 2, ipadx=20, ipady=18, padx=10, pady=10)

Player = Label(game, text = 'Зараз ходить ' + player, font = ('Comic Sans Microsoft', 14))
Player.grid()

game.mainloop()