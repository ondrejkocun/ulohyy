import tkinter
canvas = tkinter.Canvas()
canvas.pack()
x=0
y=0
canvas.create_line(280, 10, 208, 300)
canvas.create_line(350, 10, 278, 300)
for i in range(1, 20):
    canvas.create_line(273 + x, 20 + y, 358 + x, 20 + y)
    x = x - 4
    y = y + 15
