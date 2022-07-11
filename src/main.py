#Game Instructions : Dodge the asteroids. Use Arrow keys Up, Down, Left, Right to Dodge the asteroids and get a high score as possible. 
import turtle
import math
import random
import time


def run_game():
    t = 1
    num = 20
    sdf = []
    points = 0
    bnm = "bg2.gif"

    wn = turtle.Screen()
    wn.title("Dodge Asteroids by Babailan, Ronald D.")
    wn.setup(width=600, height=600)
    wn.cv._rootwindow.resizable(False, False)
    wn.tracer(0)
    wn.bgpic("background.gif")

    turtle.register_shape("player1.gif")
    turtle.register_shape("asteroid.gif")
    turtle.register_shape("gameover.gif")

    #Game over 
    gameover = turtle.Turtle()
    gameover.shape("gameover.gif")
    gameover.penup()
    gameover.hideturtle()
    gameover.goto(25, 0)

    # Player   
    pa = turtle.Turtle()
    pa.speed(0)
    pa.shape("player1.gif")
    pa.penup()
    pa.goto(0, 0)

    # Score Board
    p = turtle.Turtle()
    p.speed(0)
    p.color("white")
    p.penup()
    p.hideturtle()
    p.goto(260, 260)
    p.write("0", align="center", font=("Courier", 26, "normal"))

    # Choose a number of asteroid
    number_of_enemies = 15

    # Creat an empty list of asteroid
    enemies = []

    # Add asteroid to the list
    for i in range(number_of_enemies):
        # create the asteroid
        enemies.append(turtle.Turtle())

    for enemy in enemies:
        enemy.speed(0)
        enemy.shape("asteroid.gif")
        enemy.penup()
        enemy_random_direction = [random.randint(-280, -100), random.randint(100, 280)]
        enemy_position =random.choice(enemy_random_direction)
        y =  random.randint(-280, 280)
        enemy.goto(enemy_position, y)
        enemy.dx = 2
        enemy.dy = 2

    #Movement of player
    def pa_up():
        y = pa.ycor()
        y += 20
        pa.sety(y)

    def pa_down():
        y = pa.ycor()
        y -= 20
        pa.sety(y)

    def pa_left():
        x = pa.xcor()
        x -= 20
        pa.setx(x)

    def pa_right():
        x = pa.xcor()
        x += 20
        pa.setx(x)

    #Restarting the Game
    def reset_game():
        wn.clearscreen()
        run_game()

    # For collision between asteroid and player    
    def isCollision_enemy_player(t1, t2):
        distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
        if distance < 30:
            return True
        else:
            return False

    # Create keyboard bindings
    wn.listen()
    wn.onkeypress(pa_up, "Up")
    wn.onkeypress(pa_down, "Down")
    wn.onkeypress(pa_left, "Left")
    wn.onkeypress(pa_right, "Right")
    wn.onkeypress(reset_game, "r")


    # Main game loop
    Game_Over = False
    while True:

        p.clear()
        p.write("{}".format(points), align="center", font=("Courier", 26, "normal"))

        points += 1
        time.sleep(0.005)

        wn.update()

        enemy_random_direction = [-300, 300]
        enemy_position = random.choice(enemy_random_direction)
        
        for enemy in enemies:
            # Move the enemy
            enemy.setx(enemy.xcor() + enemy.dx)
            enemy.sety(enemy.ycor() + enemy.dy)

            if enemy.ycor() > 300:
                enemy.sety(enemy_position)
                enemy.dy *= -1

            if enemy.ycor() < -300:
                enemy.sety(enemy_position)
                enemy.dy *= -1
                    
            if enemy.xcor() > 300:
                enemy.setx(enemy_position)
                enemy.dx *= -1

            if enemy.xcor() < -300:
                enemy.setx(enemy_position)
                enemy.dx *= -1

            if pa.ycor() > 280:
                pa.sety(280)

            if pa.ycor() < -280:
                pa.sety(-280)

            if pa.xcor() > 280:
                pa.setx(280)

            if pa.xcor() < -280:
                pa.setx(-280)
                    
            if (isCollision_enemy_player(pa, enemy)):
                Game_Over = True
                break
        if Game_Over == True:
            break

    
    wn.bgcolor("red")
    pa.hideturtle()
    gameover.showturtle()

    # Main game loop
    gameover_info = turtle.Turtle()
    gameover_info.speed(0)
    gameover_info.color("white")
    gameover_info.penup()
    gameover_info.hideturtle()
    gameover_info.goto(0, -250)
    gameover_info.write("Press 'R' to Restart", align="center", font=("Courier", 19, "normal"))

    for e in enemies:
        e.hideturtle()
        
    wn.update()


run_game()

        




