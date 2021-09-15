import turtle
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

    turtle.done()
sad()