import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Catch Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# Create the player turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("white")
player.penup()

# Set up the player's movement functions
def move_left():
    x = player.xcor()
    x -= 20
    player.setx(x)

def move_right():
    x = player.xcor()
    x += 20
    player.setx(x)

# Create keyboard bindings
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Create the food items
foods = []
food_colors = ["red", "blue", "green", "yellow", "orange"]

for _ in range(10):
    food = turtle.Turtle()
    food.shape("circle")
    food.color(random.choice(food_colors))
    food.penup()
    food.goto(random.randint(-280, 280), random.randint(200, 250))
    foods.append(food)

# Set up the score
score = 0
scoreboard = turtle.Turtle()
scoreboard.color("white")
scoreboard.penup()
scoreboard.goto(-280, 260)
scoreboard.hideturtle()
scoreboard.write("Score: {}".format(score), align="left", font=("Courier", 16, "normal"))

# Main game loop
while True:
    screen.update()

    # Move the food items
    for food in foods:
        food.sety(food.ycor() - 2)

        # Check for collision with the player
        if food.distance(player) < 20:
            score += 1
            scoreboard.clear()
            scoreboard.write("Score: {}".format(score), align="left", font=("Courier", 16, "normal"))
            food.goto(random.randint(-280, 280), random.randint(200, 250))

        # Check if food item goes out of bounds
        if food.ycor() < -280:
            food.goto(random.randint(-280, 280), random.randint(200, 250))

