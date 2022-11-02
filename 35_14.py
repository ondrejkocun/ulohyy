import tkinter,random
canvas = tkinter.Canvas(height=1000,width=1000)
canvas.pack()
canvas.delete('all')

# ykreslenie pozadia
canvas.create_rectangle(0, 0, 1000, 800, fill='green', outline='')
x = 0

# vykreslenie mlak
for _ in range(1000):
    y = random.randint(20, 70)
    canvas.create_line(x, y, x, 800 - y, fill='white')
    x += 1

# pocet mlak
cislo = random.randint(20, 50)

# priemerne mlak za dlzku canvasu
kolko = 1000 // cislo
x = 10

# vykreslenie mlak
for _ in range(cislo):
    velkost = random.randint(20, 100)
    vyska = random.randint(130, 680)
    canvas.create_oval(x - velkost / 2, vyska - velkost / 2, x + velkost / 2, vyska + velkost / 2, fill='blue',
    outline='')
    x += kolko

x = 0

# vykreslenie rebrika
for _ in range(10):
    canvas.create_rectangle(x, 350, x + 100, 450, outline='brown', width=3)
    x += 100
