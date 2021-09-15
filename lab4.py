import turtle

def main():
    myTurtle=turtle.Turtle()
    s=turtle.Screen()
    pen = turtle.Turtle()
    
    square(4, pen)
    pen.up()
    pen.forward(100)
    pen.down()
    ngon(12, 20, pen)

    input()
    myScreen.exitonclick()


def square(size, pen):
    for x in range(4):
        pen.forward(100)
        pen.right(90)


def ngon(n, size, pen):
    for x in range(n):
        pen.forward(size)
        pen.right(360/n)



main()