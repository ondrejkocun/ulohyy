import tkinter
canvas = tkinter.Canvas()
canvas.pack()
def a():
    for i in range(20):
        canvas.create_line(175,200,i*40,20)
def b():
    for i in range(20):
            canvas.create_line(10,10,i*40,400)
            
def c():
    for i in range(20):
        canvas.create_line(400,280,i*20,10)
        
