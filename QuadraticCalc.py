import math


def main():
    expressions = input('Enter your quadratic expression, separating terms and operators with a space, including 1 in'
                'coefficient\n e.g. "1X^2 - 17000x - 43.679"\n')

    constituents = expressions.split(' ')

    if len(constituents) == 5:
        a = int(constituents[0][0])
        b = int(constituents[1][0] + constituents[2][0])
        c = int(constituents[3][0] + constituents[4])
    elif len(constituents) == 3:
        a = int(constituents[0][0])
        b = 0
        c = int(constituents[1][0] + constituents[2])
    elif len(constituents) == 1:
        a = int(constituents[0][0])
        b = 0
        c = 0
    else:
        a = 0
        b = 0
        c = 0

    # x = (-b +/- sqrt(b^2 - 4ac))/2

    print(str(a) + ' ' + str(b) + ' ' + str(c))
    print(type(a))
    print(type(b))
    print(type(c))

    if (b**2 - (4 * a * c)) < 0:
        x1 = 'NaN'
        x2 = 'NaN'
    else:
        x1 = (-b + math.sqrt(b**2 - (4 * a * c))) / 2
        x2 = (-b - math.sqrt(b**2 - (4 * a * c))) / 2

    print('bounds: ' + str(x1) + ' and ' + str(x2))


if __name__ == "__main__":
    main()
