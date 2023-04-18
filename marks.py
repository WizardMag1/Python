marks = []

num_exams = int(input("Введите количество экзаменов: "))

for i in range(num_exams):
    mark = int(input(f"Введие оценку за экзамен {i+1}: "))
    marks.append(mark)

sum_marks = sum(marks)
avg_marks = sum_marks / num_exams

print(f"Количество экзаменов {num_exams}, средний балл по экзаменам {avg_marks}")

