import turtle
turtle.Screen().bgcolor("pink")
board = turtle.Turtle()
board.fillcolor("lightblue")
board.begin_fill()

board.forward(100)

board.left(120)
board.forward(100)
board.left(120)
board.forward(100)


board.penup()
board.right(150)
board.forward(65)

board.pendown()
board.right(90)
board.forward(100)
board.right(120)
board.forward(100)
board.right(120)
board.forward(100)

board.end_fill()

turtle.done()