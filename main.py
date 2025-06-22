import turtle
import time
import random

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Turtle Race")
screen.setup(width=1000, height=600)

FONT = ("Arial", 24, "bold")
FINISH_LINE_X = 400

# Universal drawer turtle for intro and countdown
ui_turtle = turtle.Turtle()
ui_turtle.hideturtle()
ui_turtle.penup()
ui_turtle.color("white")

def intro_screen():
    ui_turtle.goto(0, 50)
    ui_turtle.write("Welcome to\nTurtle Race", align="center", font=("Arial", 36, "bold"))
    ui_turtle.goto(0, -50)
    ui_turtle.write("Get Ready...", align="center", font=FONT)
    time.sleep(3)
    ui_turtle.clear()

def countdown():
    for count in ["3", "2", "1", "GO!"]:
        ui_turtle.clear()
        ui_turtle.goto(0, 0)
        ui_turtle.write(count, align="center", font=("Arial", 50, "bold"))
        time.sleep(1)
    ui_turtle.clear()

def draw_track():
    track_drawer = turtle.Turtle()
    track_drawer.hideturtle()
    track_drawer.speed(0)
    track_drawer.pensize(3)
    track_drawer.color("white")

    # Start line
    track_drawer.penup()
    track_drawer.goto(-400, 200)
    track_drawer.pendown()
    track_drawer.goto(-400, -200)

    # Finish line
    track_drawer.penup()
    track_drawer.goto(FINISH_LINE_X, 200)
    track_drawer.pendown()
    track_drawer.goto(FINISH_LINE_X, -200)

    # Midline
    track_drawer.penup()
    track_drawer.goto(-400, 0)
    track_drawer.pendown()
    track_drawer.goto(FINISH_LINE_X, 0)

    # Perfectly spaced MOD positions
    mod_positions = [-200, 0, 200]
    for pos in mod_positions:
        # Lower label
        track_drawer.penup()
        track_drawer.goto(pos, -130)
        track_drawer.pendown()
        track_drawer.write(f"MOD {mod_positions.index(pos)+1}", font=FONT)

        # Upper label
        track_drawer.penup()
        track_drawer.goto(pos, 160)
        track_drawer.pendown()
        track_drawer.write(f"MOD {mod_positions.index(pos)+1}", font=FONT)

    # Title
    track_drawer.penup()
    track_drawer.color("red")
    track_drawer.goto(-100, 230)
    track_drawer.write("INTERNSHIP RACE", font=("Arial", 28, "bold"))

def create_racer(color, y_pos):
    racer = turtle.Turtle()
    racer.shape("turtle")
    racer.color(color)
    racer.penup()
    racer.goto(-400, y_pos)
    racer.pendown()
    return racer

def start_race():
    racer1 = create_racer("blue", -50)
    racer2 = create_racer("yellow", 50)
    rolls = [0, 1, 2, 3, 4, 5]

    while True:
        for racer in [racer1, racer2]:
            racer.forward(random.choice(rolls))
            if racer.xcor() >= FINISH_LINE_X:
                racer.write("WINNER!", font=FONT)
                return

# Run the program
intro_screen()
countdown()
draw_track()
start_race()

screen.mainloop()
