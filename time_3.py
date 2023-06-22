cost = int(input("Введите стоимость:"))
kol = int(input("Введите количество:"))
skidka = int(input("Введите скидку:"))

choise = input("Что вы хотите сделать посчитать стоимость одной приставки или всех ")

if choise =="одной":
    odna = cost / skidka
    print(int(odna))

skidka -= 100
skidka /= 100

print(skidka)

if choise =="всех":
    odna = cost * skidka * kol
    print(abs(int(odna)))