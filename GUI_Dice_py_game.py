from tkinter import *
import random
                                                                                                            


root= Tk()
root.geometry("600x500+0+0")
root.title("Dice Simulater" )
lbl = Label(root,font=("Time new roman",300,'bold'),text="\u2680",fg="blue")
def rolldice():
    dice=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    lbl.configure(text=f'{random.choice(dice)}')
    lbl.pack()

btn = Button(root,font=("Time new roman",25,'bold'),text="Dice Roll",command=rolldice,bg="blue",fg="white")
btn.pack()

root.mainloop()