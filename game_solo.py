from tkinter import *
from tkinter import messagebox as mb
import random
import threading

game = Tk()
game.title("Tic Tac Toe")

game.geometry("")

app = Frame(game)
app.grid()


def Bot():
    try:
        if player != "X":
            x = random.randint(0, 8)
            if x == 0:
                if (topLeft['text'] != ''):
                    Bot()
                else:
                    tl()
            #хід у ліву клітинку верхнього рядку
            elif x == 1:
                if (topMid['text'] != ''):
                    Bot()
                else:
                    tm()
            #хід у середню клітинку верхнього ряду
            elif x == 2:
                if (topRight['text'] != ''):
                    Bot()
                else:
                    tr()
            #хід у праву клітинку верхнього ряду
            elif x == 3:
                if (midLeft['text'] != ''):
                    Bot()
                else:
                    ml()
            #хід у ліву клітинку середнього ряду
            elif x == 4:
                if (midMid['text'] != ''):
                    Bot()
                else:
                    mm()
            #хід у середню клітинку середнього ряду
            elif x == 5:
                if (midRight['text'] != ''):
                    Bot()
                else:
                    mr()
            #хід у праву клітинку середнього ряду
            elif x == 6:
                if (botLeft['text'] != ''):
                    Bot()
                else:
                    bl()
            #хід у ліву клітинку нижнього ряду
            elif x == 7:
                if (botMid['text'] != ''):
                    Bot()
                else:
                    bm()
            #хід у середню клітинку нижнього ряду
            elif x == 8:
                if (botRight['text'] != ''):
                    Bot()
                else:
                    br()
            #хід у праву клітинку нижнього ряду
    except RecursionError:
        win()

XO = [[0,0,0], [0,0,0], [0,0,0]]
def win():
    if((XO[0][0] == 1 and XO[1][0] == 1 and XO[2][0] == 1) or 
       (XO[0][1] == 1 and XO[1][1] == 1 and XO[2][1] == 1) or 
       (XO[0][2] == 1 and XO[1][2] == 1 and XO[2][2] == 1) or
       #пройшла перевірка стовбців, кожен з рядків над коментарем перевіряє окремий стовбець на перемогу гравця
       (XO[0][0] == 1 and XO[0][1] == 1 and XO[0][2] == 1) or 
       (XO[1][0] == 1 and XO[1][1] == 1 and XO[1][2] == 1) or
       (XO[2][0] == 1 and XO[2][1] == 1 and XO[2][2] == 1) or 
       #пройшла перевірка рядків, кожен з рядків над коментарем перевіряє окремий рядок на перемогу гравця
       (XO[0][0] == 1 and XO[1][1] == 1 and XO[2][2] == 1) or 
       (XO[0][2] == 1 and XO[1][1] == 1 and XO[2][0] == 1)):
        #пройшла перевірка діагоналей, кожний з рядків над коментарем перевіряє окрему діагоналя на перемогу гравця
        mb.showinfo('Congratulation', 'Ви перемогли')
        game.destroy()
    elif((XO[0][0] == 2 and XO[1][0] == 2 and XO[2][0] == 2) or 
         (XO[0][1] == 2 and XO[1][1] == 2 and XO[2][1] == 2) or 
         (XO[0][2] == 2 and XO[1][2] == 2 and XO[2][2] == 2) or
         #пройшла перевірка стовбців, кожен з рядків над коментарем перевіряє окремий стовбець на перемогу компьютера
         (XO[0][0] == 2 and XO[0][1] == 2 and XO[0][2] == 2) or 
         (XO[1][0] == 2 and XO[1][1] == 2 and XO[1][2] == 2) or
         (XO[2][0] == 2 and XO[2][1] == 2 and XO[2][2] == 2) or 
         #пройшла перевірка рядків, кожен з рядків над коментарем перевіряє окремий рядок на перемогу компьютера
         (XO[0][0] == 2 and XO[1][1] == 2 and XO[2][2] == 2) or 
         (XO[0][2] == 2 and XO[1][1] == 2 and XO[2][0] == 2)):
        #пройшла перевірка діагоналей, кожен з рядків над коментарем перевіряє окрему діагональ на перемогу компьютера
        mb.showinfo('Not funny', "Вас здолав комп'ютер")
        game.destroy()
    elif(XO[0][0] != 0 and XO[1][0] != 0 and XO[2][0] != 0 and
         XO[0][1] != 0 and XO[1][1] != 0 and XO[2][1] != 0 and
         XO[0][2] != 0 and XO[1][2] != 0 and XO[2][2] != 0 and
         XO[0][0] != 0 and XO[0][1] != 0 and XO[0][2] != 0 and 
         XO[1][0] != 0 and XO[1][1] != 0 and XO[1][2] != 0 and
         XO[2][0] != 0 and XO[2][1] != 0 and XO[2][2] != 0 and 
         XO[0][0] != 0 and XO[1][1] != 0 and XO[2][2] != 0 and
         XO[0][2] != 0 and XO[1][1] != 0 and XO[2][0] != 0):
        #пройшла перевірка усіх значень списку, якщо переможець не буде виявлен до цього моменту, буде об'явлено нічию
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
        topLeft['text'] = player
        change_player()
        win()
        game.after(1000, Bot)
    else:
        mb.showerror('Шахрай', 'Ви не можете змінювати поставлений знак. Це суперечить правилам гри.') 


def tm():
    if topMid['text'] == '':
        if player == 'X':
            XO[0][1] = 1
        else:
            XO[0][1] = 2
        topMid['text'] = player
        change_player()
        win()
        game.after(1000, Bot)
    else:
        mb.showerror('Шахрай', 'Ви не можете змінювати поставлений знак. Це суперечить правилам гри.') 


def tr():
    if topRight['text'] == '': 
        if player == 'X':
            XO[0][2] = 1
        else:
            XO[0][2] = 2
        topRight['text'] = player
        change_player()
        win()
        game.after(1000, Bot)
    else:
        mb.showerror('Шахрай', 'Ви не можете змінювати поставлений знак. Це суперечить правилам гри.') 


def ml():
    if midLeft['text'] == '':
        if player == 'X':
            XO[1][0] = 1
        else:
            XO[1][0] = 2
        midLeft['text'] = player
        change_player()
        win()
        game.after(1000, Bot)
    else:
        mb.showerror('Шахрай', 'Ви не можете змінювати поставлений знак. Це суперечить правилам гри.') 


def mm():
    if midMid['text'] == '': 
        if player == 'X':
            XO[1][1] = 1
        else:
            XO[1][1] = 2
        midMid['text'] = player
        change_player()
        win()
        game.after(1000, Bot)
    else:
        mb.showerror('Шахрай', 'Ви не можете змінювати поставлений знак. Це суперечить правилам гри.') 


def mr():
    if midRight['text'] == '': 
        if player == 'X':
            XO[1][2] = 1
        else:
            XO[1][2] = 2
        midRight['text'] = player
        change_player()
        win()
        game.after(1000, Bot)
    else:
        mb.showerror('Шахрай', 'Ви не можете змінювати поставлений знак. Це суперечить правилам гри.') 


def bl():
    if botLeft['text'] == '':
        if player == 'X':
            XO[2][0] = 1
        else:
            XO[2][0] = 2
        botLeft['text'] = player
        change_player()
        win()
        game.after(1000, Bot)
    else:
        mb.showerror('Шахрай', 'Ви не можете змінювати поставлений знак. Це суперечить правилам гри.') 


def bm():
    if botMid['text'] == '': 
        if player == 'X':
            XO[2][1] = 1
        else:
            XO[2][1] = 2
        botMid['text'] = player
        change_player()
        win()
        game.after(1000, Bot)
    else:
        mb.showerror('Шахрай', 'Ви не можете змінювати поставлений знак. Це суперечить правилам гри.') 


def br():
    if botRight['text'] == '':
        if player == 'X':
            XO[2][2] = 1
        else:
            XO[2][2] = 2
        botRight['text'] = player
        change_player()
        win()
        game.after(1000, Bot)

    else:
        mb.showerror('Шахрай', 'Ви не можете змінювати поставлений знак. Це суперечить правилам гри.') 



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