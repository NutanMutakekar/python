
def print_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()
    for i in range(rows - 1, 0, -1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()

rows = 5
print_pattern(rows)