import turtle
import time


wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Python Turtle Clock")
wn.setup(width=600, height=600)


clock_face = turtle.Turtle()
clock_face.speed(0)
clock_face.pensize(3)
clock_face.color("white")


clock_face.penup()
clock_face.goto(0, -210)
clock_face.pendown()
clock_face.begin_fill()
clock_face.circle(210)
clock_face.color("gray10")
clock_face.end_fill()


clock_face.color("white")
for i in range(12):
    clock_face.penup()
    clock_face.goto(0, 0)
    clock_face.setheading(90 - (i * 30))
    clock_face.forward(180)
    clock_face.pendown()
    clock_face.forward(30)


hour_hand = turtle.Turtle()
hour_hand.speed(0)
hour_hand.pensize(6)
hour_hand.color("white")
hour_hand.shape("arrow")
hour_hand.shapesize(0.5, 8)


minute_hand = turtle.Turtle()
minute_hand.speed(0)
minute_hand.pensize(4)
minute_hand.color("white")
minute_hand.shape("arrow")
minute_hand.shapesize(0.4, 12)


second_hand = turtle.Turtle()
second_hand.speed(0)
second_hand.pensize(2)
second_hand.color("red")
second_hand.shape("arrow")
second_hand.shapesize(0.3, 14)


clock_face.penup()
clock_face.goto(0, 0)
for i in range(1, 13):
    clock_face.penup()

    angle = 90 - (i * 30)
    clock_face.setheading(angle)
    clock_face.forward(160)
    clock_face.write(str(i), align="center", font=("Arial", 20, "bold"))

clock_face.hideturtle()

while True:

    current_time = time.localtime()
    hour = current_time.tm_hour % 12
    minute = current_time.tm_min
    second = current_time.tm_sec


    hour_angle = 90 - ((hour * 30) + (minute / 2))
    hour_hand.setheading(hour_angle)

    wn.update()
    time.sleep(1)
