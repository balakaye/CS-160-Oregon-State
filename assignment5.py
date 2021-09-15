import random
import turtle

try:
    num = int(input('How many emojis do you want?(1-5): '))
except:
    print('Error: not a valid number')

pen = turtle.Turtle()

def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)

def heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()

def smiley():
    lion = turtle.Turtle()
    lion.up()
    lion.goto(0, -100)
    lion.down()

    lion.begin_fill()
    lion.fillcolor('yellow')
    lion.circle(100)
    lion.end_fill()

    lion.up()
    lion.goto(-67, -40)
    lion.setheading(-60)
    lion.width(5)
    lion.down()
    lion.circle(80, 120)
    lion.fillcolor('black')

    for i in range(-35, 105, 70):
        lion.up()
        lion.goto(i, 35)
        lion.setheading(0)
        lion.down()
        lion.begin_fill()
        lion.circle(10)
        lion.end_fill()

def sad():
    smiles = turtle.Turtle()

    smiles.goto(0,0)
    smiles.begin_fill()
    smiles.fillcolor('blue')
    smiles.circle(150)
    smiles.end_fill()

    smiles.penup()
    smiles.goto(-75,150)
    smiles.pendown()
    smiles.begin_fill()
    smiles.fillcolor('white')
    smiles.circle(10)
    smiles.end_fill()

    smiles.penup()
    smiles.goto(75, 150)
    smiles.pendown()
    smiles.begin_fill()
    smiles.fillcolor('white')
    smiles.circle(10)
    smiles.end_fill()

    smiles.penup()
    smiles.goto(0,100)
    smiles.width(5)
    smiles.pendown()
    smiles.circle(-50, 90)

    smiles.penup()
    smiles.setheading(180) 
    smiles.goto(0,100)
    smiles.width(5)
    smiles.pendown()
    smiles.circle(50, 90)

def mad():
    smiles = turtle.Turtle()

    smiles.goto(0,0)
    smiles.begin_fill()
    smiles.fillcolor('red')
    smiles.circle(150)
    smiles.end_fill()

    smiles.penup()
    smiles.goto(-75,150)
    smiles.pendown()
    smiles.begin_fill()
    smiles.fillcolor('white')
    smiles.circle(10)
    smiles.end_fill()

    smiles.penup()
    smiles.goto(-55,170)
    smiles.pendown()
    smiles.goto(-85, 190)

    smiles.penup()
    smiles.goto(75, 150)
    smiles.pendown()
    smiles.begin_fill()
    smiles.fillcolor('white')
    smiles.circle(10)
    smiles.end_fill()

    smiles.penup()
    smiles.goto(55, 170)
    smiles.pendown()
    smiles.goto(85, 190)

    smiles.penup()
    smiles.goto(0,100)
    smiles.width(5)
    smiles.pendown()
    smiles.circle(-50, 90)

    smiles.penup()
    smiles.setheading(180)
    smiles.goto(0,100)
    smiles.width(5)
    smiles.pendown()
    smiles.circle(50, 90)

def shock():
    smiles = turtle.Turtle()

    smiles.begin_fill()
    smiles.fillcolor('yellow')
    smiles.circle(100)
    smiles.end_fill()

    smiles.penup()
    smiles.goto(-35,150)
    smiles.pendown()
    smiles.begin_fill()
    smiles.fillcolor('white')
    smiles.circle(7)
    smiles.end_fill()

    smiles.penup()
    smiles.goto(35, 150)
    smiles.pendown()
    smiles.begin_fill()
    smiles.fillcolor('white')
    smiles.circle(7)
    smiles.end_fill()

    smiles.penup()
    smiles.goto(0,50)
    smiles.pendown()
    smiles.begin_fill()
    smiles.fillcolor('black')
    smiles.circle(-15)
    smiles.end_fill()

mylist = [heart, smiley, sad, mad, shock]
for x in range (num):
    x = random.choice(mylist)()

s = turtle.Screen()
s.exitonclick()
