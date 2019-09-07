import turtle


def drawSquares(l, d):
    if d == 0:
        pass
    else:
        for x in range(1, 5):
            turtle.forward(l)
            turtle.left(90)
            if x % 2 == 0:
                drawSquares(l/2, d-1)


def main():
    turtle.reset()
    smaller_dim = min(turtle.window_height(), turtle.window_width())
    # Don't have this size window? Too bad, fu
    turtle.setup(smaller_dim, smaller_dim)
    turtle.setworldcoordinates(-20, -20, 1020, 1020)
    turtle.speed(0)
    turtle.down()

    turtle.tracer(0, 0)

    drawSquares(1000, 16)
    turtle.update()
    turtle.done()

if __name__ == "__main__":
    main()
