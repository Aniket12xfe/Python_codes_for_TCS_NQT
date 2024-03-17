def find_difference(num):
    odd_sum = sum(int(num[i]) for i in range(len(num)) if i % 2 == 0)
    even_sum = sum(int(num[i]) for i in range(len(num)) if i % 2 == 1)
    return even_sum - odd_sum

# Test the function with the provided example
num = "4567"
print(find_difference(num))
