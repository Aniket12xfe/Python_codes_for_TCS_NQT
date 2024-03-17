# keyword arguments **kwargs

def fun(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

fun(name = "Aniket",roll_no =  101)


def findsum(a, b, *args):
    sm = 1
    for i in args:
        sm *= i
    return sm


# Driver's code
z = findsum(1, 2, 3, 4, 5)
print(z)