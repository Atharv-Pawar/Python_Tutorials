num = [10, 5, 8, 20, 15, 3]

largest_number = float('-inf')
second_largest_number = float('-inf')

for i in num:
    if i > largest_number:
        second_largest_number = largest_number
        largest_number = i

    elif i > second_largest_number and i != largest_number:
        second_largest_number = i

print(second_largest_number)