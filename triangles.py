import turtle

def draw_triangle(angie):
        
        angie.left(60)
        angie.forward(20)
        angie.right(120)
        angie.forward(20)
        angie.left(120)
        angie.forward(20)
        angie.right(120)
        angie.forward(20)
        angie.left(120)
        angie.forward(20)
        angie.right(120)
        angie.forward(20)
        angie.left(120)
        angie.forward(20)
        angie.right(120)
        angie.forward(20)
        angie.left(120)
        angie.forward(20)
        angie.right(120)
        angie.forward(20)
        angie.left(120)
        angie.forward(20)
        angie.right(120)
        angie.forward(20)
        angie.left(120)
        angie.forward(20)
        angie.right(120)
        angie.forward(20)
        angie.left(120)
        angie.forward(20)
        angie.right(120)
        angie.forward(20)
        angie.left(120)
        angie.right(60)
        angie.backward(160)

        #now the bigger triangle for 40 units
        angie.left(60)
        angie.forward(40)
        angie.right(120)
        angie.forward(40)
        angie.left(120)
        angie.forward(40)
        angie.right(120)
        angie.forward(40)
        angie.left(120)
        angie.forward(40)
        angie.right(120)
        angie.forward(40)
        angie.left(120)
        angie.forward(40)
        angie.right(120)
        angie.forward(40)
        angie.left(120)
        angie.right(60)
        angie.backward(160)

        #biggest tirangle
        angie.left(60)
        angie.forward(80)
        angie.right(120)
        angie.forward(80)
        angie.left(120)
        angie.forward(80)
        angie.right(120)
        angie.forward(80)
        angie.left(120)

        #going back to the upper trianlge
        angie.left(60)
        angie.forward(80)
        angie.left(60)
        angie.forward(80)
        #making smaller triangles again
        angie.right(120)
        angie.forward(20)
        angie.right(120)
        angie.forward(20)
        angie.left(120)
        angie.forward(20)
        angie.right(120)
        angie.forward(20)
        angie.left(120)
        angie.forward(20)
        angie.right(120)
        angie.forward(20)
        angie.left(120)
        angie.forward(20)
        angie.right(120)
        angie.forward(20)
        angie.left(120)
        #bigger ones
        angie.right(60)
        angie.backward(80)
        angie.left(60)
        angie.forward(40)
        angie.right(120)
        angie.forward(40)
        angie.left(120)
        angie.forward(40)
        angie.right(120)
        angie.forward(40)
        angie.left(120)
        #above this
        angie.left(60)
        angie.forward(40)
        angie.left(60)
        angie.forward(40)
        angie.right(120)
        #smaller
        angie.forward(20)
        angie.right(120)
        angie.forward(20)
        angie.left(120)
        angie.forward(20)
        angie.right(120)
        angie.forward(20)
        angie.left(120)
        #bigger
        angie.right(60)
        angie.backward(40)
        angie.left(60)
        angie.forward(40)
        angie.right(120)
        angie.forward(60)
        #extra triangle in between
        angie.forward(60)
        angie.right(120)
        angie.forward(40)
        angie.right(120)
        angie.forward(20)
        angie.right(120)
        angie.forward(20)
        angie.left(120)
        angie.forward(20)
        angie.right(120)
        angie.forward(20)
        angie.left(120)
        angie.left(60)
        angie.forward(20)
        angie.left(60)
        angie.forward(20)
        angie.backward(20)
        angie.left(120)
        angie.forward(60)
        angie.right(120)
        angie.forward(160)
        angie.right(120)
        angie.forward(60)
        angie.right(120)
        angie.forward(20)
        angie.left(120)
        angie.forward(20)
        angie.right(120)
        angie.forward(20)
        angie.left(120)
        angie.right(60)
        angie.backward(40)
        angie.left(60)
        angie.forward(20)
        angie.right(60)
        angie.forward(20)
        angie.backward(20)
        angie.right(120)
        angie.forward(40)
        angie.left(120)
        angie.forward(20)
        angie.right(60)
        angie.forward(20)
        angie.left(120)
        angie.forward(20)
        angie.right(60)
        angie.forward(20)
        angie.right(60)
        angie.forward(20)
        angie.left(120)
        angie.forward(20)
        angie.right(60)
        angie.forward(20)
        angie.right(60)
        angie.forward(20)
        angie.left(120)
        angie.forward(20)
        angie.right(60)
        angie.forward(20)
        angie.left(120)
        angie.forward(80)
        angie.left(60)
        angie.forward(20)
        angie.left(60)
        angie.forward(20)
        angie.right(120)
        angie.forward(20)
        angie.left(60)
        angie.forward(20)
        angie.right(120)
        angie.forward(40)
        angie.right(60)
        angie.forward(20)
        
   
def draw_art():
    window=turtle.Screen()
    window.bgcolor("white")
    brad=turtle.Turtle()
    brad.speed(20)
    draw_triangle(brad)
    draw_tri1()
    
    

draw_art()

