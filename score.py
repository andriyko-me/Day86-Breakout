import turtle


class ScoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.pencolor((128, 128, 128))
        self.goto(400, 350)
        self.pendown()
        self.setheading(180)
        self.current_score = 0
        self.max_score = 0

    def set_start(self, max_score: int):
        self.forward(800)
        self.penup()
        self.max_score = max_score
        self.goto(200, 370)

    def update_scoreboard(self, value):
        self.current_score += value
        self.clear()
        self.write('Score: {} / Max Score: {}'.format(self.current_score, self.max_score), font=('Arial', 16, 'bold'))

