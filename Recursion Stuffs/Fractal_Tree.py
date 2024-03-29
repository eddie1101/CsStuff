import turtle

# COLORS = ('Red', 'Green', 'Brown', 'Orange', 'Blue', 'Indigo', 'Violet')
COLORS = ('Brown', 'Green')

div = 3

def init():
    turtle.tracer(0,0)
    turtle.pensize(3)
    turtle.speed(0)
    turtle.up()
    turtle.left(90)
    turtle.backward(400)
    turtle.down()

def draw_tree(length, depth):
    turtle.color(COLORS[depth % len(COLORS)])
    turtle.forward(length)
    if depth > 1:
        turtle.left(45)
        draw_tree(length - (length / div), depth - 1)
        turtle.right(90)
        draw_tree(length - (length / div), depth - 1)
        turtle.left(45)
        turtle.color(COLORS[depth % len(COLORS)])
    if(depth % 8 == 0):
        turtle.update()
    turtle.back(length)

def main():
    init()
    draw_tree(300, 12)
    turtle.update()
    turtle.mainloop()

if __name__ == "__main__":
    main()