import tkinter,random
canvas = tkinter.Canvas()
canvas.pack()
def bengoro():
    for i in range(20):
        cislo=random.randrange(1,5)
        canvas.create_line(i*5,50,i*5,150,width=cislo)
        print(cislo)
bengoro()
