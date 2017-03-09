import turtle

def draw_diamond(angie):
    for i in range(1,5):
        angie.forward(100)
        angie.right(60)
        angie.forward(100)
        angie.right(120)
        angie.forward(100)
        angie.right(60)
        angie.forward(100)
        
     

    
def draw_art():
    window=turtle.Screen()
    window.bgcolor("white")
    brad=turtle.Turtle()
    brad.color("yellow")
    for i in range(1,73):
        draw_diamond(brad)
        brad.right(5)
   
draw_art()

    
