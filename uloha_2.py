import tkinter
import random

canvas = tkinter.Canvas(width=800, height=400)
canvas.pack()

s = random.randrange(5)
nohy = [10, 10, 5, -20, 30]
stopa = [tkinter.PhotoImage(file="stopy0.png"),
         tkinter.PhotoImage(file="stopy1.png"),
         tkinter.PhotoImage(file="stopy2.png"),
         tkinter.PhotoImage(file="stopy3.png"),
         tkinter.PhotoImage(file="stopy4.png")]

zviera = [tkinter.PhotoImage(file="zviera0.png"),
          tkinter.PhotoImage(file="zviera1.png"),
          tkinter.PhotoImage(file="zviera2.png"),
          tkinter.PhotoImage(file="zviera3.png"),
          tkinter.PhotoImage(file="zviera4.png")]

for i in range(len(zviera)):
    canvas.create_image(100+150*i, 100,
                        image=zviera[i], tags=(f"z{i}", "zviera"))

canvas.create_image(100, 350,
                    image=stopa[s], tags=(f"s{s}","stopa"))
canvas.update()

def klik(event):
    z_tag = canvas.gettags("current")[0]
    if z_tag[-1]==str(s):
        canvas.tag_unbind("zviera", "<Button-1>")
        canvas.create_image(100, 300+nohy[s],
                            image=zviera[s], tags="pohyb_z")
        canvas.update()
        canvas.after(500)
        for i in range(1, 9):
            canvas.create_image(100+i*70, 350,
                                image=stopa[s])
            canvas.move("pohyb_z", 70, 0)
            canvas.update()
            canvas.after(500)
    else:
        return None

canvas.tag_bind("zviera", "<Button-1>", klik)
