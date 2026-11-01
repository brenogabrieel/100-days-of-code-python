import turtle
import math
import random

speed_player = 15
speed_enemy = 2
speed_missil = 20
state_missil = 'ready'
enemys = []
n_enemys = 5

score = 0
n_lifes = 5
lifes = []
level = 0

screen = turtle.Screen()
screen.setup(700, 700)
screen.bgcolor('black')
screen.title('Space Invaders')

edge = turtle.Turtle()
edge.color('white')
edge.speed(0)
edge.ht()
edge.penup()
edge.setpos(-300, -300)
edge.pendown()
edge.pensize(3)
for side in range(4):
    edge.forward(600)
    edge.left(90)

player = turtle.Turtle()
player.speed(0)
player.penup()
player.color('blue')
player.shape('triangle')
player.setpos(0, -260)
player.setheading(90)

for i in range(n_enemys):
    enemy = turtle.Turtle()
    enemy.speed(0)
    enemy.penup()
    enemy.shape('circle')
    enemy.color('red')
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setpos(x, y)
    enemys.append(enemy)

missil = turtle.Turtle()
missil.speed(0)
missil.penup()
missil.color('yellow')
missil.shape('triangle')
missil.shapesize(0.5, 0.5)
missil.setheading(90)
missil.ht()

score_display = turtle.Turtle()
score_display.speed(0)
score_display.penup()
score_display.ht()
score_display.color('white')
score_display.setpos(-290, 270)
score_display.write(f'Score: {score}', font=('Arial', 14, 'bold'))

for i in range(n_lifes):
    life = turtle.Turtle()
    life.speed(0)
    life.ht()
    life.penup()
    life.shape('circle')
    life.color('yellow')
    life.setpos(-320 + i * 35, 300)
    life.st()
    lifes.append(life)

level_display = turtle.Turtle()
level_display.ht()
level_display.speed(0)
level_display.color('white')
level_display.penup()
level_display.setpos(220, 270)
level_display.write(f'Level: {level}', font=('Arial', 14, 'bold'))


def move_left():
    x = player.xcor()
    x -= speed_player
    if x <= -280:
        x = -280
    player.setx(x)


def move_right():
    x = player.xcor()
    x += speed_player
    if x >= 280:
        x = 280
    player.setx(x)


def shooting():
    global state_missil
    if state_missil == 'ready':
        state_missil = 'shooting'
        x = player.xcor()
        y = player.ycor() + 10
        missil.setpos(x, y)
        missil.showturtle()


def collision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False


turtle.listen()
turtle.onkeypress(move_left, 'Left')
turtle.onkeypress(move_right, 'Right')
turtle.onkey(shooting, 'space')

while True:
    if score > 100 and score % (100 * level) == 0:
        level += 1
        n_enemys *= level
        level_display.clear()
        level_display.write(f'Level: {level}', font=('Arial', 14, 'bold'))
        if len(enemys) <= 30:
            for _ in range(level):
                enemy = turtle.Turtle()
                enemy.speed(0)
                enemy.shape('circle')
                enemy.color('red')
                enemy.penup()
                x = random.randint(-200, 200)
                y = random.randint(100, 250)
                enemy.setpos(x, y)
                enemys.append(enemy)

    for enemy in enemys:
        if enemy.ycor() < -280:
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setpos(x, y)
        x = enemy.xcor()
        x += speed_enemy
        enemy.setx(x)
        if enemy.xcor() > 280 or enemy.xcor() < -280:
            for i in enemys:
                y = i.ycor()
                y -= 30
                i.sety(y)
            speed_enemy *= -1
        if collision(missil, enemy):
            score += 10
            score_display.clear()
            score_display.write(f'Score: {score}', font=('Arial', 14, 'bold'))
            missil.ht()
            state_missil = 'ready'
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setpos(x, y)

        if collision(player, enemy):
            if n_lifes > 0:
                x = random.randint(-200, 200)
                y = random.randint(100, 250)
                enemy.setpos(x, y)
                n_lifes -= 1
                lifes[n_lifes].ht()
                continue
            else:
                player.ht()
                enemy.ht()
                screen.clear()
                gameover = turtle.Turtle()
                gameover.speed(0)
                gameover.ht()
                gameover.penup()
                gameover.color('gray')
                gameover.setpos(-200, 0)
                gameover.write('Game over!', font=('Arial', 50, 'normal'))
                break

    y = missil.ycor()
    y += speed_missil
    missil.sety(y)
    if missil.ycor() > 270:
        missil.ht()
        state_missil = 'ready'

screen.mainloop()
