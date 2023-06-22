storage = (int(input("Размер файла в гиг:")))
speed = (int(input("Введите скорость интернета в битах:")))

choise = (input("С какой скоростью скачаеться min hour sec "))

storage *= 1024 * 1024 * 1024 *8
storage /= speed

if choise == "min":
    storage /= speed
    print(abs(int(storage)))
if choise == "hour":
    storage /= speed
    print(abs(int(storage)))
if choise == "sec":
    storage /= speed
    print(abs(int(storage)))



