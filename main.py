from turtle import Turtle, Screen


def front_move():
    dom.forward(10)


def back_move():
    dom.back(10)


def right_move():
    dom.right(5)


def left_move():
    dom.left(5)


def clear():
    dom.clear()
    dom.penup()
    dom.home()
    dom.pendown()


dom = Turtle()
screen = Screen()


screen.listen()
screen.onkey(key="w", fun=front_move)
screen.onkey(key="s", fun=back_move)
screen.onkey(key="d", fun=right_move)
screen.onkey(key="a", fun=left_move)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
