def array_sum(num , n):
    sum = 0
    for i in range(n):
        sum += num[i]
    print(sum)

arr = [1, 2, 3, 4, 5]
n = len(arr)
sum_arr = sum(arr)
print(sum_arr, end=" ")
array_sum(arr, n)
