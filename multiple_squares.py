import turtle

def draw_square(age):
        for i in range(0,4):
    #move forward
            age.forward(100)
    #turn right
            age.right(90)
def draw_art():
    #add a window
    window=turtle.Screen()
    window.bgcolor("red")
    #hold a turtule
    brad=turtle.Turtle()
    #change shape color and speed
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
draw_art()



