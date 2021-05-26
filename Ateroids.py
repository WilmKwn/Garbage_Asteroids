import turtle
import random
import math

myBorder = turtle.Turtle()
myBorder.color("black")
myBorder.shape("triangle")
myBorder.penup()
myBorder.goto(-250,-250)
myBorder.pendown()
myBorder.pensize(3)
for side in range(4):
    myBorder.forward(500)
    myBorder.left(90)
myBorder.hideturtle()

player = turtle.Turtle()
player.color("blue")
player.shape("turtle")
player.penup()
player.speed(0)
screen = player.getscreen()
turtle.bgcolor("lime")
#turtle.bgpic("space.png")

a1 = turtle.Turtle()
a1.color("green")
a1.shape("classic")
a1.penup()
a1.speed()
a1.goto(-250, -250)

a2 = turtle.Turtle()
a2.color("red")
a2.shape("circle")
a2.penup()
a2.speed(0)
a2.goto(random.randint(-240, 230), random.randint(-240, 230))

a3 = turtle.Turtle()
a3.color("red")
a3.shape("circle")
a3.penup()
a3.speed(0)
a3.goto(random.randint(-240, 230), random.randint(-240, 230))

a4 = turtle.Turtle()
a4.color("red")
a4.shape("circle")
a4.penup()
a4.speed(0)
a4.goto(random.randint(-240, 230), random.randint(-240, 230))

a5 = turtle.Turtle()
a5.color("red")
a5.shape("circle")
a5.penup()
a5.speed(0)
a5.goto(random.randint(-240, 230), random.randint(-240, 230))

a6 = turtle.Turtle()
a6.color("red")
a6.shape("circle")
a6.penup()
a6.speed(0)
a6.goto(random.randint(-240, 230), random.randint(-240, 230))

a7 = turtle.Turtle()
a7.color("red")
a7.shape("circle")
a7.penup()
a7.speed(0)
a7.goto(random.randint(-240, 230), random.randint(-240, 230))

a8 = turtle.Turtle()
a8.color("red")
a8.shape("circle")
a8.penup()
a8.speed(0)
a8.goto(random.randint(-240, 230), random.randint(-240, 230))

a9 = turtle.Turtle()
a9.color("red")
a9.shape("circle")
a9.penup()
a9.speed(0)
a9.goto(random.randint(-240, 230), random.randint(-240, 230))

a10 = turtle.Turtle()
a10.color("red")
a10.shape("circle")
a10.penup()
a10.speed(0)
a10.goto(random.randint(-240, 230), random.randint(-240, 230))


def turnleft():
    player.left(30)

def turnright():
    player.right(30)

screen.onkeypress(turnleft, "Left")
screen.onkeypress(turnright, "Right")
screen.listen()

score = 0


while True:
    player.forward(13)
    a1.forward(4.5)
    a2.forward(2)
    a3.forward(2)
    a4.forward(2)
    a5.forward(2)
    a6.forward(2)
    a7.forward(2)
    a8.forward(2)
    a9.forward(2)
    a10.forward(2)

    if player.xcor() > 250 or player.xcor() < -250:
        player.right(180)
    elif player.ycor() > 250 or player.ycor() < -250:
        player.right(180)

    dd = math.sqrt(math.pow(player.xcor()-a2.xcor(),2) + math.pow(player.ycor()-a2.ycor(),2))
    if dd < 20:
        a2.hideturtle()
        score += 1
        print(score)

    ddd = math.sqrt(math.pow(player.xcor()-a3.xcor(),2) + math.pow(player.ycor()-a3.ycor(),2))
    if ddd < 20:
        a3.hideturtle()
        score += 1
        print(score)

    dddd = math.sqrt(math.pow(player.xcor()-a4.xcor(),2) + math.pow(player.ycor()-a4.ycor(),2))
    if dddd < 20:
        a4.hideturtle()
        score += 1
        print(score)

    ddddd = math.sqrt(math.pow(player.xcor()-a5.xcor(),2) + math.pow(player.ycor()-a5.ycor(),2))
    if ddddd < 20:
        a5.hideturtle()
        score += 1
        print(score)

    dddddd = math.sqrt(math.pow(player.xcor()-a6.xcor(),2) + math.pow(player.ycor()-a6.ycor(),2))
    if dddddd < 20:
        a6.hideturtle()
        score += 1
        print(score)

    ddddddd = math.sqrt(math.pow(player.xcor()-a7.xcor(),2) + math.pow(player.ycor()-a7.ycor(),2))
    if ddddddd < 20:
        a7.hideturtle()
        score += 1
        print(score)

    dddddddd = math.sqrt(math.pow(player.xcor()-a8.xcor(),2) + math.pow(player.ycor()-a8.ycor(),2))
    if dddddddd < 20:
        a8.hideturtle()
        score += 1
        print(score)

    ddddddddd = math.sqrt(math.pow(player.xcor()-a9.xcor(),2) + math.pow(player.ycor()-a9.ycor(),2))
    if ddddddddd < 20:
        a9.hideturtle()
        score += 1
        print(score)
        

    dddddddddd = math.sqrt(math.pow(player.xcor()-a10.xcor(),2) + math.pow(player.ycor()-a10.ycor(),2))
    if dddddddddd < 20:
        a10.hideturtle()
        score += 1
        print(score)

    if a2.xcor() > 250 or a3.xcor() > 250 or a4.xcor() > 250 or a5.xcor() > 250 or a6.xcor() > 250 or a7.xcor() > 250 or a8.xcor() > 250 or a9.xcor() > 250 or a10.xcor() > 250:
        a2.left(180)
        a3.left(180)
        a4.left(180)
        a5.left(180)
        a6.left(280)
        a7.left(180)
        a8.left(180)
        a9.left(180)
        a10.left(180)

    if a2.xcor() > -250 or a3.xcor() > -250 or a4.xcor() > -250 or a5.xcor() > -250 or a6.xcor() > -250 or a7.xcor() > -250 or a8.xcor() > -250 or a9.xcor() > -250 or a10.xcor() > -250:
        a2.left(180)
        a3.left(180)
        a4.left(180)
        a5.left(180)
        a6.left(280)
        a7.left(180)
        a8.left(180)
        a9.left(180)
        a10.left(180) 


    if a1.xcor() > 250:
        a1.hideturtle()
        a2.hideturtle()
        a3.hideturtle()
        a4.hideturtle()
        a5.hideturtle()
        a6.hideturtle()
        a7.hideturtle()
        a8.hideturtle()
        a9.hideturtle()
        a10.hideturtle()
        player.hideturtle()
        print("Your Time Ran Out!!!!")
        turtle.write("Your Time Ran Out")




