def median_fun(arr, n):
    arr.sort()
    if n % 2 == 0:
        return (arr[n // 2]-1 + arr[n // 2])/2
    else:
        return arr[n // 2]


def average(arr, n):
    sum = 0
    for i in range(n):
        sum += arr[i]
    print(sum//n)

arr = [1,2,3,4,5]
n = len(arr)
print(median_fun(arr, n))
average(arr, n)