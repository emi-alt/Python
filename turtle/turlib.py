import turtle 
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(500,600)
poly = turtle.Turtle()

num = 5
a = 100
angle = 360.00/num

for i in range(num):
    poly.forward(a)
    poly.right(angle)

turtle.done()