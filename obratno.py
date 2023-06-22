start = int(input("Введите начальное число: "))
end = int(input("Введите конечное число: "))

for num in range(end, start - 1, -1):
    print(num)
