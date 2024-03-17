row = 3
# for i in range(1, row+1):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()

for i in range(row):
    for j in range(row - i):
        print("*", end=" ")
    print()
# for i in range(row, 0, -1):
#     print("* " * i)


# for i in range(1, row+1):
#     print("* " * i)

