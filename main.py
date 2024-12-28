import turtle

# Screen setup
wn = turtle.Screen()
wn.title("PONG by Daniel (@zendayasbrother)")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:  # Prevent going off-screen
        y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -250:  # Prevent going off-screen
        y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:  # Prevent going off-screen
        y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -250:  # Prevent going off-screen
        y -= 20
    paddle_b.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main Game Loop
while True:
        wn.update()

        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border Checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1  # Reverse direction

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1  # Reverse direction

        if ball.xcor() > 390:
            ball.goto(0, 0)  # Reset position
            ball.dx *= -1  # Reverse direction

        if ball.xcor() < -390:
            ball.goto(0, 0)  # Reset position
            ball.dx *= -1  # Reverse direction


