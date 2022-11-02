import tkinter
canvas = tkinter.Canvas()
canvas.pack()
def strom():
    canvas.create_rectangle(50,80,80,150,fill='brown')
    canvas.create_oval(30,50,100,110,fill='green')
    canvas.create_line(80,80,75,90,fill='brown',width=3)
    canvas.create_line(80,80,85,90,fill='brown',width=3)
    canvas.create_oval(70,88,80,98,fill='red')
    canvas.create_oval(90,88,80,98,fill='red')
strom()
