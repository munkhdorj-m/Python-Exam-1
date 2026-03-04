# Exercise 1
def time_to_seconds(hours, minutes, s):
    return hours * 3600 + minutes * 60 + s

# Exercise 2
def years_months_to_months(years, months):
    return years * 12 + months


# Exercise 3
def max_of_two(a, b):
    if a > b:
        return a
    return b


# Exercise 4
def sum_greater_than_80(a, b, c, d):
    total = 0
    for num in [a, b, c, d]:
        if num > 80:
            total += num
    return total


# Exercise 5 (PRINT)
def print_ioi(n):
    for _ in range(n):
        print("IOI")


# Exercise 6 (RETURN)
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Exercise 7 (PRINT)
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n}*{i}={n*i}")


# Exercise 8 (PRINT)
def print_pattern(n):
    for i in range(1, n + 1):
        for _ in range(i):
            print(i, end=" ")
        print()
