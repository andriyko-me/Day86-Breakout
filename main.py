from turtle import Screen
import time
import os
from user_plt import Platform
from ball import Ball
from blocks import Block
from score import ScoreBoard
import gc

colors = [(102, 204, 0), (255, 255, 0), (204, 102, 0), (204, 0, 0)]

# ----------------------------------- Screen and Canvas objects
screen = Screen()

screen.colormode(255)
screen.bgcolor((32, 32, 32))
canvas = screen.getcanvas()
scoreboard = ScoreBoard()

screen.tracer(0)

# ----------------------------------- Game Objects ------------------------------------------------

platform = Platform()
ball = Ball()
ball.setheading(270)
blocks = []


# ----------------------------------- Functions ------------------------------------------------


def position(event):
    """ Moves platform after the mouse """
    x_cor = event.x - 450
    platform.goto(x_cor, platform.ycor())


def create_row():
    """ Creates rows of blocks """
    for color in colors:
        for num in range(24):
            new_block = Block()
            new_block.showturtle()
            new_block.fillcolor(color)
            new_block.setposition(x=450 - 40 * num, y=100 + 40 * colors.index(color))
            blocks.append(new_block)


def get_block_price(b_block: Block):

    """ Gives value to +score """
    if b_block.fillcolor() == colors[2] or b_block.fillcolor() == colors[3]:
        return 4
    else:
        return 2


def get_max_score():
    if os.path.exists('max_score.txt'):
        pass
    else:
        with open('max_score.txt', 'w') as file:
            file.write('0')

    with open('max_score.txt', 'r') as file:
        num = int(file.read())
    return num


def rewrite_max_score():
    with open('max_score.txt', 'w') as file:
        file.write(f'{scoreboard.current_score}')


max_score = get_max_score()
canvas.bind('<Motion>', position)
game_is_on = True
create_row()
scoreboard.set_start(max_score)
scoreboard.update_scoreboard(0)
ball.setheading(95)
# ---------------------------------------------- The Game ------------------------------------------------------

while game_is_on:
    ball.forward(10)
    game_is_on = ball.check_position(platform)

    for block in blocks:
        if ball.distance(block.xcor(), block.ycor()) < 40:

            scoreboard.update_scoreboard(get_block_price(block))
            blocks.remove(block)
            block.reset()
            block.hideturtle()
            gc.collect()
            ball.backward(20)
            ball.setheading(360 - ball.heading())
        if len(blocks) == 0:
            create_row()

    screen.update()
    time.sleep(.005)

screen.exitonclick()

if scoreboard.current_score > max_score:
    rewrite_max_score()
