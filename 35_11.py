import tkinter,random
canvas = tkinter.Canvas(width=1000)
canvas.pack()
farba=['red','blue','brown','pink','purple','orange','green','yellow']
x=0
for i in range(20):
    polomer=random.randrange(50,100)
    pol=polomer//2
    canvas.create_oval(x,100-pol,x+polomer+pol,100+polomer,width=3,outline=random.choice(farba))
    x+=50
