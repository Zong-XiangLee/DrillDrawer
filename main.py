import turtle


# football field 2.25:1
turtle.home()

#football field 810 wide 360 tall
turtle.setup(width=(1010), height=(560))
turtle.bgcolor('green')
turtle.title("Drill Viewer")

turtle.penup()
turtle.pencolor('white')
turtle.pensize(3)
turtle.goto(-405,-180)
turtle.pendown()
turtle.goto(405,-180)
turtle.goto(405,180)
turtle.goto(-405,180)
turtle.goto(-405,-180)

turtle.mainloop()
