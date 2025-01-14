import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Random Star Shapes")
screen.bgcolor("black")

# Create turtle for drawing stars
star_turtle = turtle.Turtle()
star_turtle.speed(0)
star_turtle.hideturtle()

# Define a function to draw a star
def draw_star(size, color):
    angle = 144
    star_turtle.color(color)

    star_turtle.begin_fill()
    for _ in range(5):
        star_turtle.forward(size)
        star_turtle.right(angle)
        star_turtle.forward(size)
        star_turtle.right(72 - angle)
    star_turtle.end_fill()

# Set up the random attributes for stars
colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "white"]
min_size = 10
max_size = 100
num_stars = 50

# Draw the stars
for _ in range(num_stars):
    x = random.randint(-screen.window_width()//2, screen.window_width()//2)
    y = random.randint(-screen.window_height()//2, screen.window_height()//2)
    size = random.randint(min_size, max_size)
    color = random.choice(colors)
    
    star_turtle.penup()
    star_turtle.goto(x, y)
    star_turtle.pendown()
    
    draw_star(size, color)

# Exit the program when the screen is clicked
screen.exitonclick()
