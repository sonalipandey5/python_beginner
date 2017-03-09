import turtle

def initials(sp):
    sp.backward(100)
    sp.right(90)
    sp.forward(100)
    sp.left(90)
    sp.forward(100)
    sp.right(90)
    sp.forward(100)
    sp.right(90)
    sp.forward(100)
    sp.backward(100)
    sp.left(180)
    sp.penup()
    sp.forward(50)
    sp.pendown()
    sp.left(90)
    sp.forward(200)
    sp.right(90)
    sp.forward(100)
    sp.right(90)
    sp.forward(100)
    sp.right(90)
    sp.forward(100)






def art():
    window=turtle.Screen()
    window.bgcolor("light blue")
    brad=turtle.Turtle()
    brad.color("dark blue")
    initials(brad)
art()
