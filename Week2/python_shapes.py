
side_length = 50


#square
colors_list = ["red", "blue", "green"]

def square(color):
    pencolor(color)
    pendown()
    for i in range(4):
        forward(side_length)
        right(90)
    penup()
    forward(60)

def colored_squares():
    for x in colors_list:
        square(x)

colored_squares()




#triangle
color_list = ["red", "orange", "yellow", "green", "blue", "purple", "black"]

def triangle(color):
    pencolor(color)
    pendown()
    for i in range(3):
        forward(side_length)
        left(120)
    penup()
    forward(5)

def colored_triangles():
    for x in color_list:
        triangle(x)

colored_triangles()

pencolor("pink")
for i in range(120):
    for i in range(3):
        pendown()
        forward(50)
        left(120)
    penup()
    forward(5)

def regular_polygon(number_of_sides,side_length,side_color):
    pencolor(color)
    pendown()
    for i in range(number_of_sides):
        forward(side_length)
        right((180*(number_of_sides - 2)
        right(number_of_sides - 2

