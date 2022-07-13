import random
import turtle
from tkinter import simpledialog


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # TODO 1) Create a new Turtle
    new_turtle = turtle.getturtle()
    #      2) Make the turtle draw a shape (this will take more than one line
    #         of code)
    new_turtle.pendown()
    #new_turtle.forward(25)
    #new_turtle.left(25)
    #new_turtle.forward(25)
    #new_turtle.left(25)
    #      3) Set the pen width to 10
    new_turtle.width(10)
    while True:
    #      4) Ask the user what color pen they would like to draw with
     user_input = simpledialog.askstring(prompt="pen color", title=" what color of pen would you like ? ")
    #      5) Use an if/else statement to set the pen color that the user
    #         requested
     if user_input == "red":
         for i in range(4):
          new_turtle.pencolor("red")
          new_turtle.pendown()
          new_turtle.forward(100)
          new_turtle.left(90)

         break
    #      6) If the user doesn't enter anything, choose a random color
     elif user_input == "":
      new_turtle.pencolor(get_random_color())
      new_turtle.pendown()
      new_turtle.forward(100)
      new_turtle.left(90)

    #      7) Put a loop around your code so that you keep asking the user for
    #         more colors & drawing them
    pass
    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
