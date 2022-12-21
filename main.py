from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

my_snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(my_snake.snake_up, "Up")
screen.onkey(my_snake.snake_down, "Down")
screen.onkey(my_snake.snake_left, "Left")
screen.onkey(my_snake.snake_right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    sleep(0.1)
    my_snake.move_snakes()

    if my_snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()
        my_snake.expand()

    if my_snake.head.xcor() > 290 or my_snake.head.xcor() < -290 or my_snake.head.ycor() > 290 or my_snake.head.ycor() < -290:
        game_is_on = False
        score.set_game_over()

    for i in my_snake.snakes[1:]:
        if my_snake.head.distance(i) < 10:
            game_is_on = False
            score.set_game_over()

    my_snake.counter = 0

screen.exitonclick()
