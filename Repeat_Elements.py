def find_repeating_elements(arr):
    seen = set()
    repeating_elements = set()

    for i in arr:
        if i in seen:
            repeating_elements.add(i)
        else:
            seen.add(i)
    return list(repeating_elements)

arr = [1, 1, 2, 3, 4, 4, 5, 2]
print(find_repeating_elements(arr))