def reverse_fun(Number):
    reverse_arr = Number[::-1]
    print(reverse_arr)

def internal_fun(nums):
    return ''.join(reversed(nums))

def reverse_number(ber):
    ber.reverse()
    print(ber)


num = "hello i am aniket chaudhari"
ber = [5,4,3,2,1]
n = len(num)
reverse_fun(num)
reverse_number(ber)
print(internal_fun(num))