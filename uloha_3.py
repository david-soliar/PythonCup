import tkinter
import random

M = random.randint(3,5)
N = random.randint(3,7)

canvas = tkinter.Canvas(width=N*50, height=M*50)
canvas.pack()

duch = tkinter.PhotoImage(file="duch.png")

stvorce = dict()
y = 0
for m in range(M):
    x = 0
    for n in range(N):
        stvorec = str(m)+str(n)
        stvorce[stvorec] = (x+25, y+25)
        canvas.create_rectangle(x, y,
                                x+50, y+50,
                                fill=random.choice(("white", "gray")),
                                tags=(stvorec, "s"))
        x += 50
    y += 50
canvas.update()

duch_zobrazenie = random.randint(3, 5)
for i in range(duch_zobrazenie):
    stvorec = str(random.randrange(M)) + str(random.randrange(N))
    x, y = stvorce[stvorec]
    canvas.create_image(x, y, image=duch, tags="duch")
    canvas.update()
    canvas.after(500)
    canvas.delete("duch")

def klik(event):
    global x, y
    c = canvas.gettags("current")[0]
    x1, y1 = stvorce[c]
    if x==x1 and y==y1:
        canvas.create_image(x, y, image=duch, tags="duch")
        canvas.create_text(x+20, y+20,
                           text="SUPER",
                           fill="red")
    else:
        canvas.create_image(x, y, image=duch, tags="duch")
        canvas.create_text(x+20, y+20,
                           text="TU SOM",
                           fill="red")

    canvas.tag_unbind("s", "<Button-1>")

canvas.tag_bind("s", "<Button-1>", klik)
