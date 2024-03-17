def accenting_descending(nums, n):
    nums.sort()
    for i in range(n//2):
        print(nums[i], end=" ")
    for j in range(n -1, n // 2-1, -1):
        print(nums[j], end=" ")



nums = [8,7,1,6,5,9]
n = len(nums)
accenting_descending(nums, n)
