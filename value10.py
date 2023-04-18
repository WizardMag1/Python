while True:
    num1 = int(input("Введите первое число"))
    num2 = int(input("Введите второе число"))
    if num1 + num2 == 10:
        print("Сумма чисел равна 10")
        break
    elif num1 + num2 > 10:
        print("Сумма больше 10")
