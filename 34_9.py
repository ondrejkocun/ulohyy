import tkinter
canvas = tkinter.Canvas()
canvas.pack()
for i in range(2):
    canvas.create_line(i*20+10,50,i*20+50,250)
for i in range(1,20):
    canvas.create_line(i*2+10,i*10+50,i*2+30,i*10+50)
