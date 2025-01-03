def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_numbers = []
average = calculate_average(my_numbers)
print(f"The average is: {average}")