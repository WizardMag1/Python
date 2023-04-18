films = []

Parts = int(input("Введиет количество частей фильма:"))

for i in range(Parts):
    film = float(input(f"Введите продолжительность фильма {i+1}: "))
    films.append(film)

sum_films = sum(films)

print(f"Количество частей фильма {Parts}, Продолжительность их в сумме {sum_films}")