import math


def main():
    expressions = input('Enter your quadratic expression, separating terms and operators with a space, including 1 in'
                'coefficient\n e.g. "1X^2 - 17000x - 43.679"\n')

    constituents = expressions.split(' ')

    if len(constituents) == 5:
        a = constituents[0][0]
        b = int(constituents[1] + constituents[2])
        c = int(constituents[3] + constituents[4])
    elif len(constituents) == 3:
        a = int(constituents[0])
        b = 0
        c = int(constituents[1] + constituents[2])
    elif len(constituents) == 1:
        a = int(constituents[0])
        b = 0
        c = 0
    else:
        a = 0
        b = 0
        c = 0

    # x = (-b +/- sqrt(b^2 - 4ac))/2
    x1 = 0
    x2 = 0

    x1 = (-b + math.sqrt(b**2 - (4 * a * c))) / 2
    x2 = (-b - math.sqrt(b**2 - (4 * a * c))) / 2

    print('bounds: ' + str(x1) + ' and ' + str(x2))


if __name__ == "__main__":
    main()
