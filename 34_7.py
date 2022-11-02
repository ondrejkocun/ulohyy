import tkinter,random
canvas = tkinter.Canvas()
canvas.pack()
farba=['red','blue','brown','pink','purple','orange','green','yellow']
def a():
    for i in range(80):
        canvas.create_line(0,random.randrange(250),400,random.randrange(250),width=random.randrange(1,5),fill=random.choice(farba))
def b():
    for i in range(80):
        canvas.create_line(random.randrange(400),0,random.randrange(400),300,width=random.randrange(1,5),fill=random.choice(farba))
def c():
    for i in range(80):
        canvas.create_line(200,150,random.randrange(400),random.randrange(300),width=random.randrange(1,5),fill=random.choice(farba))

