start = int(input("Введите начальное число: "))
end = int(input("Введите конечное число: "))

for num in range(start, end + 1):
    if num % 2 == 0:
        print(num)
