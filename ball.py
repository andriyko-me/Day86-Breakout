import turtle
import random


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()

        self.shape('circle')
        self.color((51, 153, 255))
        self.penup()
        self.choose_direction()
        self.speed('fastest')
        self.angel = 0

    def choose_direction(self):
        self.setheading(to_angle=random.randint(0, 360))

    def define_angel(self, turtle_object: turtle.Turtle):
        self.angel = 90 / 2 * (
                2 - self.distance(turtle_object.xcor(), turtle_object.ycor()) / 70) \
            if self.xcor() > turtle_object.xcor() \
            else 90 / 2 * (2 + self.distance(turtle_object.xcor(), turtle_object.ycor()) / 70)

        return self.angel

    def check_position(self, platform: turtle.Turtle):
        if self.xcor() > 470 or self.xcor() < -470:
            self.setheading(180 - self.heading())
            self.forward(10)
        elif self.distance(platform.xcor(), platform.ycor()) < 35 \
                or self.distance(platform.xcor() + 70, platform.ycor()) < 35 \
                or self.distance(platform.xcor() - 70, platform.ycor()) < 35:
            self.setheading(self.define_angel(platform))
            self.forward(10)
        elif self.ycor() > 350:
            self.setheading(360 - self.heading())
            self.forward(20)

        elif self.ycor() < -370:
            return False
        return True
