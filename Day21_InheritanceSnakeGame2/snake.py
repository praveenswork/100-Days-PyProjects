from turtle  import Turtle

STARTING_POS=[(0, 0), (-20, 0), (-40, 0)]
MOVE = 20
Up = 90
Down = 270
Right = 0
Left = 180

class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]


    def create_snake(self):
        for snake_pos in STARTING_POS:
            self.add_segment(snake_pos)
            self.segment[0].color('red')

    def add_segment(self,position):
        new_seg = Turtle("square")
        new_seg.penup()
        new_seg.goto(position)
        self.segment.append(new_seg)

    def extend_snake(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            x_pos = self.segment[seg_num - 1].xcor()
            y_pos = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(x_pos, y_pos)
        self.head.forward(MOVE)

    def reset(self):
        for seg in self.segment:
            seg.goto(1000,1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]

    def up(self):
        if self.head.heading() != Down:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != Up:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != Right:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != Left:
            self.head.setheading(0)


