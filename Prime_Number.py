def check_and_prime(num):
    if num < 0:
        print("Negative number entered.")
        num = int(input("Enter a positive number: "))
        check_and_prime(num)
    elif num == 0 or num == 1:
        print(num, "is not a prime number.")
    else:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, "is a prime number.")
        else:
            print(num, "is not a prime number.")

# Input number
num = int(input("Enter a number: "))
check_and_prime(num)
