def number_palindrome(numbers):
    num = str(numbers)
    return num == num[::-1]

numbers = -123454321
print(number_palindrome(numbers))