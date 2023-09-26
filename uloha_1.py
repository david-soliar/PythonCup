from turtle import *
import random

st()
speed(0)

x = random.randint(-350, 300)
y = random.randint(100, 220)
penup()
setpos(x, y)
pendown()

n = random.randint(5, 15)
strana = random.randint(10, 20)
luc = random.randint(30, 80)

def obdlznik(a, b):
    lt(90)
    fd(b)
    lt(90)
    fd(a)
    lt(90)
    fd(b)
    lt(90)
    fd(a)

def slnko(n, strana, luc):
    uhly = 180*(n-2)
    uhol = uhly/n

    for i in range(n):
        fd(strana)
        obdlznik(strana, luc)
        rt(180-uhol)

slnko(n, strana, luc)
