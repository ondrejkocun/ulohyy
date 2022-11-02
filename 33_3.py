import tkinter
canvas = tkinter.Canvas()
canvas.pack()
def balon():
    canvas.create_oval(50,50,80,80,fill='blue')
    canvas.create_line(50,65,65,100)
    canvas.create_line(80,65,65,100)
    canvas.create_rectangle(55,100,75,105,fill='red')
balon()
