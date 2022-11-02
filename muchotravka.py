import tkinter,random
canvas = tkinter.Canvas(width=400,height=400,background='white')
canvas.pack()

x=300
y=300
x1=305
y1=305
def muchotravka():
    canvas.create_oval(100, 300, 180, 380, fill="red", outline="")
    canvas.create_rectangle(0, 330, 200, 400, fill="white", outline="")
    canvas.create_rectangle(130, 330, 150, 410, fill="brown", outline="")
    canvas.create_oval(130, 400, 150, 420, fill="brown", outline="")
    canvas.create_oval(125, 305, 130,310, fill="white", outline="red")
    canvas.create_oval(110, 320, 115, 325,fill="white", outline="red")
    canvas.create_oval(135, 320, 140, 325, fill="white", outline="red")
    canvas.create_oval(150, 310, 160, 320, fill="white", outline="red")
def trava():
    canvas.create_rectangle(0,380,400,400,fill='green',outline='')
    for i in range(40):
        canvas.create_line(i*10,370,i*10,400,fill='green',width=2)
def luce():
    for i in range(40):
        canvas.create_line(0,0,random.randrange(100),random.randrange(100),fill='yellow',width=3)

def jazero():
    global x,y,x1,y1
    for j in range(1,21):
        x=x+5
        y=y+5
        xx=xx-5
        yy=yy-5
        canvas.create_oval(x-5,y-5,xx+5,yy+5, outline="cyan")
canvas.create_rectangle(200,50,400,200,outline='')
def pozemky():
    x=150
    y=0
    for j in range(3):
           y+=55
           x=150
           for i in range(5):
                a=random.randrange(50)
                canvas.create_rectangle(x,y,x+a,y+a)
                x+=50
pozemky()
