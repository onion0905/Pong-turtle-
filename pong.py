import turtle
from time import sleep

# wn setting
wn = turtle.Screen()
wn.title("onion's pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# score
score_a = 0
score_b = 0

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

wow = turtle.Turtle()

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {}  Player B:{}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

# main game loop
while True:

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if paddle_a.ycor() > 280:
        paddle_a.sety(280)
    
    if paddle_a.ycor() < -280:
        paddle_a.sety(-280)

    if ball.ycor() > 285:
        ball.sety(280)
        ball.dy *= -1

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1

    if ball.xcor() > 380:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B:{}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -380:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B:{}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # paddle and ball collisions
    if (ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40) and (ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340) and (ball.xcor() < 350) and (ball.ycor() < paddle_a.ycor() + 40) and (ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

    if ball.dx > 0 and ball.dy > 0:
        if abs(300 - ball.ycor()) < abs(335 - ball.xcor()):
            bounce_point_x = 300 - ball.ycor() + ball.xcor()
            ballY_predict = 265 + ball.xcor() - ball.ycor()
            distance = ballY_predict - paddle_b.ycor()
            if distance >= 0:
                for count in range(int(distance)):
                    paddle_b.sety(paddle_b.ycor() + 1)
            elif distance < 0:
                for count in range(abs(int(distance))):
                    paddle_b.sety(paddle_b.ycor() - 1)

        else:
            ballY_predict = 335 - ball.xcor() + ball.ycor()
            distance = ballY_predict - paddle_b.ycor()
            if distance >= 0:
                for count in range(int(distance)):
                    paddle_b.sety(paddle_b.ycor() + 1)
            elif distance < 0:
                for count in range(abs(int(distance))):
                    paddle_b.sety(paddle_b.ycor() - 1)



    if ball.dx > 0 and ball.dy < 0:
        if abs(-300 - ball.ycor()) < abs(335 - ball.xcor()):
            bounce_point_x = ball.xcor() + ball.ycor() + 300
            ballY_predict = -265 - ball.xcor() - ball.ycor()
            distance = ballY_predict - paddle_b.ycor()
            if distance >= 0:
                for count in range(int(distance)):
                    paddle_b.sety(paddle_b.ycor() + 1)
            elif distance < 0:
                for count in range(abs(int(distance))):
                    paddle_b.sety(paddle_b.ycor() - 1)

        else:
            ballY_predict = ball.xcor() + ball.ycor() - 335
            distance = ballY_predict - paddle_b.ycor()
            if distance >= 0:
                for count in range(int(distance)):
                    paddle_b.sety(paddle_b.ycor() + 1)
            elif distance < 0:
                for count in range(abs(int(distance))):
                    paddle_b.sety(paddle_b.ycor() - 1)

    wn.update()

