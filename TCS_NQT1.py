def find_nth_term(n):
    if n % 2 == 1:
        time_in_series = (n + 1) // 2
        res = 2 ** (time_in_series - 1)
        print(res , end=" ")
    else:
        time_in_series = n // 2
        res = 3 ** (time_in_series - 1)
        print(res, end=" ")
if __name__ == "__main__":
    n = int(input())
    print(find_nth_term(n))