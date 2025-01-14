import turtle

# Create a turtle object
my_turtle = turtle.Turtle()

# Set the speed of the turtle 
my_turtle.speed(10)

# Function to draw a flower shape
def draw_flower():
    for _ in range(36):
        my_turtle.forward(100)
        my_turtle.right(45)
        my_turtle.forward(100)
        my_turtle.right(135)
        my_turtle.forward(100)
        my_turtle.right(45)
        my_turtle.forward(100)
        my_turtle.right(170)
    
# Loop to draw the flower shape all over the screen
for _ in range(10):
    draw_flower()
    my_turtle.right(36)


turtle.done()


