def sum_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

input_numbers = input().split()
numbers = [int(num) for num in input_numbers]

result = sum_numbers(numbers)
print("Sum:", result)