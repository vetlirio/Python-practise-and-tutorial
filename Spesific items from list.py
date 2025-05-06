def sum_of_odd_numbers(end):
    total = 0
    for i in range (1, end, 2):
        total += i
    return total

print(sum_of_odd_numbers(20))


def sum_of_odd_numbers(end):
    for i in range (1, end, 2):
        return i

print(sum_of_odd_numbers(20))


def print_odd_numbers(end):
    for i in range(1, end, 2):
        print(i)

(print_odd_numbers(20))