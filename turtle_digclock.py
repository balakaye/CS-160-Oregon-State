import time
import datatime as dt 
import turtle

t = turtle.Turtle()

t1 = turtle.Turtle()

s = turtle.Screen()
input()

s.bgcolor("green")

sec = dt.datetime.now().second
min = dt.datetime.now().minute
hr = dt.datetime.now().hour
t1.pensize(3)
t1.color('black')
t1.penup()

t1.goto(-20, 0)
t1.pendown()

for i in range(2):
    t1.forward(200)
    t1.left(90)
    t1.forward(70)
    t1.left(90)

t1.hideturtle()

while True:
    t.hideturtle()
    t.clear()
    #display the time
    t.write(str(hr).zfill(2))
        +":"+str(min).zfill(2)+":"
        +str(sec).zfill(2),
        font =("Arial Narrow", 35, "bold")
    timesleep(1)
    sec+= 1

    if sec == 60:
        sec = 0
        min+= 1

    if min == 60:
        min = 0
        min+= 1

    if hr == 13:
        hr = 1