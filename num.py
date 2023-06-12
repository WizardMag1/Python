numbers = []

num_numbers = int(input("Введите количество чисел:"))

for i in range(num_numbers):
    number = int(input(f"Введите число {i+1}: "))
    numbers.append(number)

highest_value = max(numbers)
print(f"Самое большое число:{highest_value}")
