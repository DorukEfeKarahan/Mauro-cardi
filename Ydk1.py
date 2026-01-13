import turtle

screen = turtle.Screen()
star = turtle.Turtle()
star.color("blue")
star.speed(5)

def draw_star():
    for _ in range(5):
        star.forward(100)
        star.right(150)

for i in range(5):
    draw_star()
    star.penup()
    star.forward(150)  
    star.pendown()

turtle.done()