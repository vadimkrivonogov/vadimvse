from tkinter import * 
from turtle import width
from PIL import ImageGrab
import io
from tkinter import font
raam = Tk()
raam.title("poland")
tahvel = Canvas(raam, width=600, height=600, background="grey")
tahvel.grid()

#poland
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


raam = Tk()
raam.title("valgusfoor")
tahvel = Canvas(raam, width=350, height=500, background="white")
tahvel.grid()




raam.mainloop()