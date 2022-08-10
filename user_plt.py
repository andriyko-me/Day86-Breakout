import turtle


class Platform(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color((51, 153, 255))
        self.shape('square')
        self.turtlesize(1, 10)
        self.penup()
        self.setposition(x=0, y=-350)





