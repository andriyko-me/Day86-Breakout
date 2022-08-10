import turtle

# 1 = 20px


class Block(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(2, 2)

        self.penup()
        self.shape('square')
        self.color((0, 0, 0))



