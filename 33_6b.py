import tkinter
canvas = tkinter.Canvas()
canvas.pack()
farba=['red','blue','brown','pink','purple','orange','green','yellow']
for i in range(8):
    canvas.create_oval(10+i*35,100,i*35+70,150,fill=farba[i])
    canvas.create_line(40+i*35,100,150,70)
