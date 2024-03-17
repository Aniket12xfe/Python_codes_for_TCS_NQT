def swap(a, b):
    a, b = b, a
    print("After swapping")
    print(a, end=', ')
    print(b)

a = 10
b = 20
print("Before swapping")
print(a, end=', ')
print(b)
swap(a, b)