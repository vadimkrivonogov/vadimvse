from tkinter import * 
from turtle import width
from PIL import ImageGrab
import io
from tkinter import font
from tkinter import * 
from turtle import window_width
from random import * 
raam = Tk()
raam.title("monako")
tahvel = Canvas(raam, width=600, height=600, background="grey")
tahvel.grid()

#monako
tahvel.create_rectangle(30,200, 300,300,fill="red")
tahvel.create_rectangle(30,300, 300,400,fill="white")

raam = Tk()
raam.title("estonia")
tahvel = Canvas(raam, width=600, height=600, background="grey")
tahvel.grid()
#estonia
tahvel.create_rectangle(650,50, 300,150,fill="blue")
tahvel.create_rectangle(650,100, 300,150,fill="black")
tahvel.create_rectangle(650,200, 300,150,fill="white")

raam = Tk()
raam.title("bahama")
tahvel = Canvas(raam, width=600, height=600, background="grey")
tahvel.grid()

#bahama
tahvel.create_rectangle(30,50, 300,150,fill="cyan")
tahvel.create_rectangle(30,100, 300,150,fill="yellow")
tahvel.create_rectangle(30,200, 300,150,fill="cyan")
tahvel.create_polygon(30,50,100,125,30,200, fill="black")

raam = Tk()
raam.title("muster")
tahvel = Canvas(raam, width=600, height=600, background="grey")
tahvel.grid()

#muster
tahvel = Canvas(raam, width=600, height=600, background="#630202")
k=7
x0=50
y0=50
x1=550
y1=550
for i in range(k):
    x0+=50
    y0+=50
    x1-=50
    y1-=50
    tahvel.create_rectangle(x0,y0,x1,y1,width=1,outline="blue", fill="#5e005c")
    tahvel.create_oval(x0,y0,x1,y1,width=1, outline="blue", fill="#00adb3")
tahvel.grid()

ps = tahvel.postscript(colormode='color')
x1=tahvel.winfo_width()
y1=tahvel.winfo_height()

ImageGrab.grab().crop((0,0,x1,y1)).save("image.jpg")

#разноцветный круг
colors = ["black",
          "white",
          "blue",
          "red",
          "pink",
          "green", 
          "yellow",
          "gold",
          "lightblue"]

raam2 = Tk()
raam2.title("разноцветный круг")
tahvel2 = Canvas(raam2, width=1200, height=1200, background="white")
x0=0
y0=0
x1=600
y1=600
p=5
for i in range(55):
    x0+=p 
    y0+=p 
    x1-=p 
    y1-=p 
    tahvel2.create_oval(x0,y0,x1,y1, fill=choice(colors))

    #doska
raam = Tk()
raam.title("Tahvel")
tahvel = Canvas(raam, width=600, height=600, background="white")

square_size = 50

for row in range(8):
    for col in range(8):
        x1 = col * square_size
        y1 = row * square_size
        x2 = x1 + square_size
        y2 = y1 + square_size
        if (row+col) % 2 == 0:
            color = "black"
        else:
            color = "white"
        tahvel.create_rectangle(x1, y1, x2, y2, fill=color)

tahvel.grid()
raam.mainloop()
