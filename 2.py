num = int(input("Введите число: "))

if num < 2:  # числа 0 и 1 не являются простыми
    print("Число не простое")
else:
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            print("Число не простое")
            break
    else:
        print("Число простое")
