import turtle

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


    turtle.done()

shock()
