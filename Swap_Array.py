def rotate_arr(num, k):
    n = len(num)
    k = k % n
    num[:] = num[-k:] + num[:-k]

arr = [1,2,3,4,5]
k = 2
rotate_arr(arr, k)
print(arr)