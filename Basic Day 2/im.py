import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Star Collector")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Create the player turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("white")
player.penup()

# Create the stars
stars = []
for _ in range(20):
    star = turtle.Turtle()
    star.shape("turtle")  # Use the "turtle" shape
    star.color("yellow")
    star.penup()
    star.goto(random.randint(-390, 390), random.randint(-290, 290))
    stars.append(star)

# Set up the keyboard bindings
def move_up():
    y = player.ycor()
    if y < 290:
        y += 20
    player.sety(y)

def move_down():
    y = player.ycor()
    if y > -290:
        y -= 20
    player.sety(y)

def move_left():
    x = player.xcor()
    if x > -390:
        x -= 20
    player.setx(x)

def move_right():
    x = player.xcor()
    if x < 390:
        x += 20
    player.setx(x)

# Keyboard bindings
screen.listen()
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Main game loop
while True:
    screen.update()

    # Move each star
    for star in stars:
        star.setx(star.xcor() - 1)

        # Check for collision with player
        if star.distance(player) < 20:
            star.goto(random.randint(-390, 390), random.randint(-290, 290))
