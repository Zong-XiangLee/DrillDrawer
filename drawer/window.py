import turtle

# football field 2.25:1


# default = 4
window_scale = int(input("Window Scale:\n"))
window_width_scale = window_scale
window_height_scale = window_scale

windowWidth = (360/2*window_width_scale + 50*window_width_scale)
# default 2
windowHeight = (180/2*window_height_scale + 50*window_height_scale)
# football field outlineWidth/2 feet wide outline_length/2 feet tall
# x2, 720x320 2 pixels = 1 foot

outlineWidth = window_width_scale*360/2
outline_length = window_height_scale*180/2


def init_window():
    turtle.home()
    turtle.setup(width=windowWidth, height=windowHeight)
    turtle.bgcolor('green')
    turtle.title("Drill Viewer")


def outline():
    turtle.penup()
    turtle.pencolor('white')
    turtle.pensize(3)
    turtle.goto(-outlineWidth/2, -outline_length/2)
    turtle.pendown()
    turtle.goto(outlineWidth/2, -outline_length/2)
    turtle.goto(outlineWidth/2, outline_length/2)
    turtle.goto(-outlineWidth/2, outline_length/2)
    turtle.goto(-outlineWidth/2, -outline_length/2)
    turtle.penup()


if window_scale == 0:
    print("hello world")
else:
    init_window()
    outline()
    turtle.mainloop()
