import tkinter,random
canvas = tkinter.Canvas(height=300,background='white')
canvas.pack()
cislo=random.randrange(50,120)
canvas.create_oval(30,100,80,150,fill='brown')
canvas.create_rectangle(0,125,400,400,fill='blue')
canvas.create_line(55,100,55,20,width=2)
canvas.create_line(55,20,120,20,120,60,55,60,width=2)
canvas.create_rectangle(55,20,120,60,fill='green')
canvas.create_oval(75,25,100,50,fill='yellow')
canvas.create_oval(85,25,100,50,fill='green',outline='green')
canvas.create_line(120,110,200,110,180,140,140,140,120,110,width=3)
canvas.create_line(160,110,160,50,180,80,160,90,width=3)
canvas.create_oval(200,125-cislo,250,125-cislo+50,fill='yellow')
canvas.create_oval(215,125-cislo,250,125-cislo+50,fill='white',outline='white')
canvas.create_oval(200,125+cislo,250,125+cislo-50,fill='yellow')
canvas.create_oval(215,125+cislo,250,125+cislo-50,fill='blue',outline='blue')