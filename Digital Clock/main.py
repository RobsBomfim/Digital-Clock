import tkinter
from tkinter import *
from datetime import datetime


color_1 = "#181e31" #black
color_2 = "#41ee33" #green

janela = Tk()
janela.title("")
janela.geometry("430x200")
janela.resizable(width=False, height=False)
janela.config(bg=color_1)

def clock():

    time = datetime.now()
    hour = time.strftime("%H:%M:%S")
    weekday = time.strftime("%A")
    day = time.day
    month = time.strftime("%b")
    year = time.strftime("%Y")  
    l1.config(text=hour)
    l1.after(210, clock)

    l2.config(text= weekday + " " + str(day) + " / " + str(month) + " / " + (year))


l1 = Label(janela, font= ("arial 80"), bg=color_1, fg=color_2)
l1.grid(row=0, column=0,sticky=NW)

l2 = Label(janela, font=("arial 20"), bg=color_1, fg=color_2)
l2.grid(row=1, column=0,sticky=NW)



clock()

janela.mainloop()