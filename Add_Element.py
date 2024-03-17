def insert_beginning(arr, element):
    arr.insert(0, element)

def insert_ending(arr, element):
    arr.append(element)

def insert_at_pos(arr, element, pos):
    arr.insert(pos, element)

# Initial array
arr = [1, 2, 3, 4, 5]

# Inserting at the beginning
insert_beginning(arr, 6)

# Inserting at the end
insert_ending(arr, 7)

# Inserting at a specific position
insert_at_pos(arr, 8, 3)

# Printing the final array
print(arr)
