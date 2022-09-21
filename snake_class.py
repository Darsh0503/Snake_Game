from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0),(-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN =270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)


    def extend(self):
        #add a new segment to snake
        self.add_segment(self.segments[-1].position())

    def move(self):
        #      range(2,0,-1) start from 2,1,0
        #      first 2 go in to the snake_num, then snakes[2-1]=snakes[1]=middle sqaure.xcor (store in to new_X)         SNAKES[0,1,2]
        #      same for new_y
        #      snakes[1] now go on the position of x_new and Y_new cordinator

        for snake_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[snake_num - 1].xcor()
            new_y = self.segments[snake_num - 1].ycor()
            self.segments[snake_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)