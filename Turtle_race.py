# Klasicka struktura:
# 1) nejdriv importy
# 2) pak funkce
# 3) nakonec main(), kde funkce pouzivam

import random
from turtle import Turtle, Screen


def main():
    colours = ["red", "orange", "yellow", "green", "blue", "purple"]
    y_coordinates_list = range(-170, 238, 68)
    start_position = -220

    screen = Screen()
    screen.setup(width=500, height=400)
    while True:  # tady je cyklus, kterej bezi, dokud uzivatel nezada existujici barvu
        user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a colour: ")
        if user_bet in colours:
            break
    print(user_bet)

    # vhodnejsi struktura je tady slovnik
    all_turtles = {colour: (Turtle(shape='turtle'), y_coord) for colour, y_coord in zip(colours, y_coordinates_list)}
    # udelal jsem slovnik, kde key je barva zelvy a value je tuple obsahujici ten objekt Turtle a jeho y souradnici
    # funkce zip bere postupne dve polozky z nichz jedna je z listu colors a druha z y_coordinates_list. Zip se hodi kdyz iterujes pres vice iterables
    for colour, (turtle_obj, y_coord) in all_turtles.items():
        #tohle mozna neni nutny schovavat do funkce: proste vezmes ten objekt Turtle a postupne pouzijes ty metody color, penup, goto
        turtle_obj.color(colour)
        turtle_obj.penup()
        turtle_obj.goto(start_position, y_coord) # tady je vhodnejsi dat promennou misto konkterni hodnoty. Hodnotu promenne si potom definujes hned na zacatku main(), potom je jednodussi se v tom vyznat

    game_on = True
    while game_on:
        for turtle, _ in all_turtles.values():
            if turtle.xcor() > - start_position:
                game_on = False
                winning_colour = turtle.pencolor()
            turtle.forward(random.randint(0, 10))

    # ten print se da naplacnout na jeden radek, ale u tehle dlouhejch to neni asi moc citelny
    print(f"The {winning_colour} turtle has won the race. You made the right bet." if  winning_colour.lower() == user_bet.lower() else f"The {winning_colour} turtle has won the race. You made the wrong bet.")
    screen.exitonclick()


if __name__ == "__main__":
    main()
