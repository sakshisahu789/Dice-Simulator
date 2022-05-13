from tkinter import*
import random

root = Tk()

root.title("Dice Simulator")

root.geometry("700x600")

label = Label(root , font = ("Montserrat" , 300 , 'bold') , text = "" , bg = 'thistle' , fg = 'navy')

def rolldice() :
    dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    label.configure(text = f'{random.choice(dice)}')
    label.pack()

button = Button(root, font = ("Heuristica" , 25 , 'bold') , text = "Dice Roll" , command = rolldice , bg = 'gold')
button.pack()

root.mainloop()
