from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a colour: ")
print(user_bet)

colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_coordinates_list = range(-170, 238, 68)

all_turtles = []
for new_turtle in colours:
    new_turtle = Turtle(shape="turtle")
    all_turtles.append(new_turtle)

def define_turtle(colour, y_coordinates):
    name.color(colour)
    name.penup()
    name.goto(-220, y_coordinates)

for i in range(len(colours)):
    name = all_turtles[i]
    define_turtle(colour=colours[i], y_coordinates=y_coordinates_list[i])

game_on = True
while game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            game_on = False
            winning_colour = turtle.pencolor()
        turtle.forward(random.randint(0, 10))

if winning_colour.lower() == user_bet.lower():
    print(f"The {winning_colour} turtle has won the race. You made the right bet.")
else:
    print(f"The {winning_colour} turtle has won the race. You made the wrong bet.")

screen.exitonclick()
