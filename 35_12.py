import tkinter
canvas = tkinter.Canvas(width=400,height=400)
canvas.pack()

for i in range(40):
    canvas.create_rectangle(i*10,0,i*10,400,width=1)
    canvas.create_rectangle(0,i*10,400,i*10,width=1)
