two_numbers = []

first_number = int(input("Введите первое число "))
second_number = int(input("Введите второе число"))

want = (input("Что вы хотите сделать:+, -, /, *,"))
if want == '+':
    sum = first_number + second_number
    two_numbers.append(sum)
print(two_numbers)
if want == '-' :
    two_numbers = first_number - second_number
if want == '/' :
    two_numbers = first_number / second_number
if want == '*' :
    two_numbers = first_number * second_number
    
    
print(two_numbers)