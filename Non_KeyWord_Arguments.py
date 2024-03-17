# non keyword arguments *args

def summation(*args):

    sm = 0

    for i in args:
        sm += i

    print(sm)

summation(2, 3, 4, 5)