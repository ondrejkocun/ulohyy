import tkinter
canvas = tkinter.Canvas()
canvas.pack()

canvas.create_oval(60,15,90,50,fill='red',outline='red')
canvas.create_oval(50,25,80,50,fill='yellow',outline='yellow')
canvas.create_oval(65,25,100,50,fill='green',outline='green')

canvas.create_line(50,50,75,150,100,50,)
canvas.create_rectangle(50,40,100,50,fill='white')
