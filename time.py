
time_second = int(input("Введите время в секундах:"))

time_second -= 86400 

choise = input("Как вы хотите считать:sec min hour ")

if choise == "min":
    time_second = time_second / 60
    print (int(abs(time_second)))
if choise == "sec":
    print (int(abs(time_second)))
if choise == "hour":
    time_second /= 60
    time_second /= 60
    print (int(abs(time_second)))    

  

