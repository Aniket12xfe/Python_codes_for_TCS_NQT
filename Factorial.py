def fact(n):
    factor = 1
    for i in range(1, n+1):
        factor = factor * i

    return factor

ans = fact(7)
print(ans)