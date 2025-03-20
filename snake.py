"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import *
import random

from freegames import square, vector

#Creamos una lista de colores
colores = ['black','blue','purple','grey','orange']

#Seleccionamos los colores de forma aleatoria
snake_color = random.choice(colores)
food_color = random.choice(colores)

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def move_food():
    """Move food to a random position."""
    directions = [(0, 10), (0, -10), (10, 0), (-10, 0)]
    
    for dx, dy in directions:
        new_pos = vector(food.x + dx, food.y + dy)
        if inside(new_pos) and new_pos not in snake:
            food.x = new_pos.x
            food.y = new_pos.y
            return


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        print('Snake:', len(snake))
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color)

    square(food.x, food.y, 9, food_color)
    update()
    ontimer(move, 100)
    move_food()


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
