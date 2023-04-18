try:
    num = int(input("Введите число: "))
    value = 1 / num
    print("Результат",value)
except ZeroDivisionError:
    print("Деление на ноль!")
except ValueError:
    print("Некоректный ввод")
except Exception as value:
    print("Ошибка", value)
else:
    print("Опирация была успешно выполнена")
finally:
    print("Програма завершина")
