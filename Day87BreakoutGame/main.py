from turtle import Turtle, Screen
from time import sleep
from paddle import Paddle
from ball import Ball
from wall import Blocks, Block
from scoreboard import Scoreboard
from ui import UI



                          # screen features


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=700)
screen.title("Pong")
screen.tracer(0)





paddle = Paddle((0, -330))
ball = Ball((0, 0))
wall = Blocks()
ui = UI()
ui.header()
score = Scoreboard(lives=5)



game_paused = False
game_is_on = True

def pause_game():
    global game_paused
    if game_paused:
        game_paused = False
    else:
        game_paused = True

screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkeypress(paddle.move_left, "Left")
screen.onkeypress(paddle.move_right, "Right")
screen.onkey(paddle.move_right, "Right")
screen.onkey(pause_game, "space")


def check_collision_with_paddle():
    if ball.distance(paddle) < 140 and ball.ycor() < -280:
        if paddle.xcor() > 0:
            if ball.xcor() > paddle.xcor():
                # If ball hits paddles left side it
                # should go back to left
                ball.bounce_x()
                ball.bounce_y()
                return
            else:
                ball.bounce_y()
                return

            # If Paddle is left of Screen
        elif paddle.xcor() < 0:
            if ball.xcor() < paddle.xcor():
                # If ball hits paddles left side it
                # should go back to left
                ball.bounce_x()
                ball.bounce_y()
                return
            else:
                ball.bounce_y()
                return

            # Else Paddle is in the Middle horizontally
        else:
            if ball.xcor() > paddle.xcor():
                ball.bounce_x()
                ball.bounce_y()
                return
            elif ball.xcor() < paddle.xcor():
                ball.bounce_x()
                ball.bounce_y()
                return
            else:
                ball.bounce_y()
                return
def check_collision_with_blocks():
    for block in wall.blocks:
        if ball.distance(block) < 40:
            score.increase_score()
            block.quantity -= 1
            if block.quantity == 0:
                block.clear()
                block.goto(3000, 3000)
                wall.blocks.remove(block)
            if ball.xcor() < block.left_wall:
                ball.bounce_x()
            elif ball.xcor() > block.right_wall:
                ball.bounce_x()
            elif ball.ycor() > block.upper_wall:
                ball.bounce_y()
            elif ball.ycor() < block.bottom_wall:
                ball.bounce_y()

def check_collision_with_walls():
    if ball.ycor() > 290:
        ball.bounce_y()
        return
    # Detect collision with x walls
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.bounce_x()
        return

def check_paddle_miss():
    if ball.ycor() < -300:
        ball.reset_position()
        score.decrease_lives()

        ui.change_color()
        return


while game_is_on:
    if not game_paused:
        screen.update()
        sleep(0.01)
        ball.move()

        #Detect paddle miss
        check_paddle_miss()

        #Detect collision with paddle
        check_collision_with_paddle()

        #Detect collision with y walls
        check_collision_with_walls()

        #Detect collision with bricks
        check_collision_with_blocks()

        if paddle.xcor() < -280:
            screen.onkeypress(None,  "Left")
            screen.onkey(None, "Left")
        else:
            screen.onkeypress(paddle.move_left, "Left")
            screen.onkey(paddle.move_left, "Left")


        if paddle.xcor() > 280:
            screen.onkeypress(None, "Right")
            screen.onkey(None, "Right")
        else:
            screen.onkeypress(paddle.move_right, "Right")
            screen.onkey(paddle.move_right, "Right")

        if score.lives == 0:
            score.reset()
            game_is_on = False
            ui.game_over(win=False)
            break

        if len(wall.blocks) == 0:
            game_is_on = False
            ui.game_over(win=True)
            break
    else:
        ui.paused_status()















screen.exitonclick()