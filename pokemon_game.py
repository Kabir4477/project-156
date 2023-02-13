# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 15:15:48 2023

@author: drsau
"""
from tkinter import *
from PIL import ImageTk,Image
root = Tk()

root.title("Endless pokemon Game")
root.geometry("600x600")

root.configure(background="chocolate1")

pikachu = ImageTk.PhotoImage(Image.open("pikachu.jpg"))
abra= ImageTk.PhotoImage(Image.open("abra.jpg"))
balbasour = ImageTk.PhotoImage(Image.open("bulbasour.jpg"))
kadabra = ImageTk.PhotoImage(Image.open("kadabra.jpg"))
nidoking = ImageTk.PhotoImage(Image.open("nidoking.jpg"))
jigglypuff = ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
paras = ImageTk.PhotoImage(Image.open("paras.jpg"))
persion = ImageTk.PhotoImage(Image.open("persion.jpg"))
ratata = ImageTk.PhotoImage(Image.open("ratata.jpg"))
squirtle = ImageTk.PhotoImage(Image.open("squirtle.jpg"))
Iyvasour = ImageTk.PhotoImage(Image.open("Iyvasour.jpg"))
button = ImageTk.PhotoImage(Image.open("button.jpg"))
charmender = ImageTk.PhotoImage(Image.open("charmender.jpg"))



player1 = Label(root,text = "Player 1" , bg = "royal blue",fg = "white")
player1.place(relx = 0.1, rely = 0.3 , anchor = CENTER)

player2 = Label(root, text = "Player 2" , bg = "royal blue" , fg = "white")
player2.place(relx = 0.9 , rely=0.3 , anchor=CENTER)

player_1_score_label  = Label(root , bg = "red",fg = "white")
player_1_score_label.place(relx=0.1 , rely=0.4 , anchor=CENTER)

player_2_score_label = Label(root , bg = "red",fg = "white")
player_2_score_label.place(relx=0.9 , rely=0.4 , anchor=CENTER)

random_dice_label = Label(root , bg ="white",fg = "black")
random_dice_label.place(relx = 0.5 , rely = 0.5 , anchor = CENTER)

root.mainloop()