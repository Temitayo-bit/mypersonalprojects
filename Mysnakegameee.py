import turtle
import time
import random

window = turtle.Screen()
window.title("T-snake")
window.bgcolor("green")
window.setup(width=500, height =500)


d = 0.1

score = 0
high_score = 0

window.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("brown")
head.penup()
head.goto(0, 0)
head.direction = "stop"



food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0, 100)

part = []


pencil = turtle.Turtle()
pencil.speed(0)
pencil.shape("square")
pencil.color("black")
pencil.penup()
pencil.hideturtle()
pencil.goto(0, 210)
pencil.write ("Score: 0  High score: 0", align = "center", font=("courier", 24, "normal"))


def up():
     if head.direction != "down":
        head.direction = "up"

def left():
     if head.direction != "right":
        head.direction = "left"

def right():
     if head.direction != "left":
        head.direction = "right"

def down():
     if head.direction != "up":
        head.direction = "down"

def go():
       if head.direction == "up":
           y = head.ycor()
           head.sety(y + 20)

       if head.direction == "down":
           y = head.ycor()
           head.sety(y - 20)

       if head.direction == "left":
           x = head.xcor()
           head.setx(x - 20)

       if head.direction == "right":
           x = head.xcor()
           head.setx(x + 20)

    

window.listen()
window.onkeypress(up, "w")
window.onkeypress(down, "s")
window.onkeypress(right, "d")
window.onkeypress(left, "a")

while True:
    window.update()
    
    if head.xcor() > 240 or head.xcor() < -240 or head.ycor() > 240 or head.ycor() < -240:
        time.sleep(0.5)
        head.goto(0,0)
        head.direction = "stop"

        for parts in part:
            parts.goto(700, 700)

        part.clear()

        score = 0

        d = 0.1
        pencil.clear()
        pencil.write("Score: {} High Score: {}".format(score, high_score), align="center", font = ("courier", 24, "normal"))



    if head.distance(food) < 20:
        x = random.randint (-240, 240)
        y = random.randint(-240, 240)
        food.goto(x,y)   

        new_part = turtle.Turtle()
        new_part.speed(0)
        new_part.shape("circle")    
        new_part.color("brown")
        new_part.penup()
        part.append(new_part)

        d -= 0.001

        score += 5

        if score > high_score:
            high_score = score
        pencil.clear()
        pencil.write("Score: {} High Score: {}".format(score, high_score), align="center", font = ("courier", 24, "normal"))

    for index in range(len(part) -1, 0, -1):
        x = part[index - 1].xcor()
        y = part[index - 1].ycor()
        part[index].goto(x,y)


    if len(part) > 0:
        x = head.xcor()
        y = head.ycor()
        part[0].goto(x,y)
         
    
    go()

    for parts in part:
        if parts.distance(head) < 20:
            time.sleep(0.5)
            head.goto(0,0)
            head.direction = "stop"

            for parts in part:
                parts.goto(700, 700)

            part.clear()

            score = 0
            d = 0.1
            pencil.clear()
            pencil.write("Score: {} High Score: {}".format(score, high_score), align="center", font = ("courier", 24, "normal"))


    time.sleep(d)
    
 
   
window.mainloop()