start = int(input("Введите начальное число: "))
end = int(input("Введите конечное число: "))

if start > end:
    start, end = end, start

for num in range(start, end ):
    if num % 2 != 0:
        print(num)