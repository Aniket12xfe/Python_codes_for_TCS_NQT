def print_divisors(n):
    Divisors = []

    for i in range(1, n+1):
        if n % i == 0:
            Divisors.append(i)
    return Divisors

N = int(input())
print(print_divisors(N))