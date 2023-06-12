year = int(input("Введите год: "))

if year % 400 == 0:
    print("Год высокосный")
else:    
    if year % 4 == 0 and year % 100 != 0:
        print("Год высокосный")
    else:
        print("Год не высокосный")