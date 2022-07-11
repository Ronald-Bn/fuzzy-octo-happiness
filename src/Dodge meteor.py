#Game Instructions : Use "a" key to go left and "d" key to go right  
import turtle
import math
import random

def run_game():

    wn = turtle.Screen()
    wn.title("Hit the bricks")
    wn.bgcolor("green")
    wn.setup(width=800, height=600)
    wn.tracer(0)

    
    # Paddle A
    paddle_a = turtle.Turtle()
    paddle_a.speed(0)
    paddle_a.shape("square")
    paddle_a.color("white")
    paddle_a.shapesize(stretch_wid=1, stretch_len=5)
    paddle_a.penup()
    paddle_a.goto(0, -240)

    # Ball
    ball = turtle.Turtle()
    ball.speed(0)
    ball.color("black")
    ball.shape("circle")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 2
    ball.dy = 2

    

    wn.update()

    # Funtion
    def paddle_a_right():
        x = paddle_a.xcor()
        x += 20
        paddle_a.setx(x)

    def paddle_a_left():
        x = paddle_a.xcor()
        x += -20
        paddle_a.setx(x)


    wn.register_shape("brick",((0,0),(20,0),(20,80),(0,80)))

    colors = ["sky blue", "tomato", "lime green","yellow"]
    
    def makeRow(x,y,colors):
      index = random.randint(0,len(colors)-1)
      row = []
      for i in range(8):
        targetT = turtle.Turtle()
        targetT.speed(0)
        targetT.shape("brick")
        targetT.color(colors[index])
        targetT.penup()
        targetT.goto(x + 100 * i,y)
        targetT.pendown()
        row.append(targetT)
        index = random.randint(0,len(colors)- 1)
      return row

    wn.update()

    def countList():
      count = []
      for i in range(8):
        count.append(0)
      return count

    def checkCollisonBrick(obj):
        if abs(ball.xcor() - obj.xcor()) < 50 and obj.ycor() <= ball.ycor() <= obj.ycor() + 10:
            print("colided with the brick:", obj)
            return True
        return False
    
    def hitBrick(row, count, goal):
      for x in range(len(row)):
    #checks to see if this specific brick collided with ball
        if checkCollisonBrick(row[x]):
      #checks if brick should disappear
          if count[x] > goal:
            row[x].ht()
            row[x].penup()
            row[x].goto(-1000,1000)
          else:
            #brick can still be hit more
            count[x] += 1
            row[x].ht()
            row[x].penup()
            row[x].goto(-1000,1000)
            y = ball.ycor()
            ball.sety(y)
            ball.dy *= -1

      return count


    def checkCollisonPaddle(obj):
      if abs(ball.xcor() - obj.xcor()) < 100 and (obj.ycor() <= ball.ycor() <= obj.ycor() + 20) :
        return True

      return False

    def try_again():
        wn.clearscreen()
        run_game()
        

    # Keyboard binding
    wn.listen()
    wn.onkeypress(paddle_a_left, "a")
    wn.onkeypress(paddle_a_right, "d")
    wn.onkeypress(try_again, "t")

    row1 = makeRow(-390,200,colors)
    count1 = countList()
    row2 = makeRow(-390,170,colors)
    count2 = countList()
    row3 = makeRow(-390,140,colors)
    count3 = countList()
    row4 = makeRow(-390,110,colors)
    count4 = countList()
    
    # Main Game Loop
    while True:
        wn.update()

        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        count1 = hitBrick(row1, count1, 4)
        count2 = hitBrick(row2, count2, 3)
        count3 = hitBrick(row3, count3, 2)
        count4 = hitBrick(row4, count4, 1)


        # Border checking
        if ball.ycor() > 300:
            ball.sety(300)
            ball.dy *= -1

        if ball.ycor() < -300:
            boundary = turtle.Turtle()
            boundary.penup()
            boundary.hideturtle()
            boundary.goto(-120,0)
            boundary.color("midnight blue")
            boundary.write("YOU LOSE!", font=("Fixedsys",32,"normal"))
            
            

        if ball.xcor() > 400:
            ball.setx(400)
            ball.dx *= -1
            
        if ball.xcor() < -400:
            ball.setx(-400)
            ball.dx *= -1
        
        # Paddle and ball collisions
        if (checkCollisonPaddle(paddle_a)):
            x = ball.xcor()
            ball.setx(x)
            ball.dy *= -1

        # Paddles can't go beyond screen
        if paddle_a.xcor() >= 400:
            paddle_a_left()
            
        if paddle_a.xcor() <= -400:
            paddle_a_right()

        
        wn.update()



run_game()
