from tkinter import *
import os

root = Tk()
root.title('Tic-Tac-Toe the Game')

L = Label(root, width = 25, text = 'Tic-Tac-Toe', font = ('Comic Sans MS', 18)) 
s = Button(root, width = 25, text = 'Start solo', font = ('Comic Sans MS', 10))
m = Button(root, width = 25, text = 'Start multiplayer', font = ('Comic Sans MS', 10))
e = Button(root, width = 25, text = 'Exit', font = ('Comic Sans MS', 10))

def solo(event):
	os.startfile('game_solo.py')
	root.destroy()

def multi(event):
	os.startfile('game_multiplayer.py')
	root.destroy()

def exit(event):
	root.destroy()

s.bind('<Button-1>', solo)
m.bind('<Button-1>', multi)
e.bind('<Button-1>', exit)

L.pack()
s.pack()
m.pack()
e.pack()
root.mainloop()