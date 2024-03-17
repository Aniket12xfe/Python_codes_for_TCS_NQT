# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(arr,n):
    visited = [False for i in range(n)]
    for i in range(n):
        if visited[i]:
            continue

        count = 1
        for j in range(i+1, n, 1):
            if arr[i] == arr[j]:
                visited[j] = True
                count += 1

        print(arr[i], count)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    array = [10,5,10,15,10,5]
    n = len(array)
    print_hi(array, n)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
