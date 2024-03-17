def is_palindrome(string):
    string = ''.join(e.lower() for e in string if e.isalnum())

    return string == string[::-1]

def two_pointers(string):
    string = string.lower()
    start, end = 0, len(string) - 1
    while start < end:
        if not string[start].isalnum():
            start += 1
        elif not string[end].isalnum():
            end -= 1
        elif string[start] != string[end]:
            return False
        else:
            start += 1
            end -= 1
    return True

print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("race a car"))
print(two_pointers("A man, a plan, a canal: Panama"))
print(two_pointers("race a car"))