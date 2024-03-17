def check(num):
    if num < 0:
        print("Negative number is entered")
        num = int(input("Enter the positive number"))
    prime(num)

def prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

num = int(input("Enter the number: "))
check(num)