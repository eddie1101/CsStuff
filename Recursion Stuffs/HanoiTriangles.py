import turtle


def shape(l, d):
    if d == 1:
        turtle.circle(l/3)
    else:
        for x in range(3):
            turtle.forward(l)
            shape(l/2, d - 1)
            turtle.left(120)


def main():
    turtle.tracer(0, 0)
    turtle.up()
    turtle.right(180)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.down()

    turtle.speed(0)

    shape(250, 9)
    turtle.update()
    turtle.mainloop()


if __name__ == "__main__":
    main()
