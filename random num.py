# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 19:59:54 2022

@author: turtl_4
"""

from tkinter import *
import random
root = Tk()
root.title("Random Numbers")
root.geometry("400x400")

label_word = Label(root)

def word():
    alpha_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    random_no1 = random.randint(1,26)
    random_no2 = random.randint(1,26)
    random_no3 = random.randint(1,26)    
    random_no4 = random.randint(1,26)
    random_no5 = random.randint(1,26)
    random_alpha1 = alpha_list[random_no1]
    random_alpha2 = alpha_list[random_no2]
    random_alpha3 = alpha_list[random_no3]
    random_alpha4 = alpha_list[random_no4]
    random_alpha5 = alpha_list[random_no5]
    label_word["text"] = random_alpha1 + random_alpha2 + random_alpha3 + random_alpha4 + random_alpha5
    




btn = Button(root,text="generate random word", command=word)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

label_word.place(relx=0.5,rely=0.6,anchor=CENTER)


root.mainloop()