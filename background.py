from tkinter import*
from PIL import ImageTk, Image
from hold import hold
class background:
   def __init__(self, root) :
     self.root = root
     global y
     y = []
     #global img
     img = Image.open("cards/" + "blue2.png")
     img = img.resize((80, 120))
     tkimage = ImageTk.PhotoImage(img)
     y.append(hold(img, tkimage))
     for i in range(7):
       for j in range (5):
       #root.configure(background='black')
         #22b14c
         Label(self.root,background = '#4391d1', image=y[0].b).grid(row=j, column=i)
         #Label(self.root,background = 'green4').grid(row=j, column = i)