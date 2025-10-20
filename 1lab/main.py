import random

random.seed(42)

students = [
    "Аня", "Борис", "Вика", "Гриша", "Даша",
    "Егор", "Женя", "Зоя", "Игнат", "Кира"
]

subjects = ["Матем.", "Физика", "Химия", "Русск.", "История"]


grades = []
for i in range(len(students)):
    row = []
    for j in range(len(subjects)):
        row.append(random.randint(2, 5))
    grades.append(row)


print("Таблица оценок:")
print("Имя\t", "\t".join(subjects))
for name, row in zip(students, grades):
    print(f"{name}\t", "\t".join(map(str, row)))


avg_per_student = []
for row in grades:
    avg = sum(row) / len(row)
    avg_per_student.append(avg)

print("\nСредние оценки студентов:")
for name, avg in zip(students, avg_per_student):
    print(f"{name}: {avg:.2f}")


max_per_subject = []
min_per_subject = []

for col in range(len(subjects)):
    column_values = [grades[row][col] for row in range(len(grades))]
    max_per_subject.append(max(column_values))
    min_per_subject.append(min(column_values))

print("\nПо предметам (макс / мин):")
for subj, mx, mn in zip(subjects, max_per_subject, min_per_subject):
    print(f"{subj}: max = {mx}, min = {mn}")


best_index = avg_per_student.index(max(avg_per_student))
worst_index = avg_per_student.index(min(avg_per_student))

best_student = students[best_index]
worst_student = students[worst_index]

print("\nСтуденты по средним баллам:")
print(f"Лучший студент: {best_student} со средним баллом {avg_per_student[best_index]:.2f}")
print(f"Худший студент: {worst_student} со средним баллом {avg_per_student[worst_index]:.2f}")


print("\nВсе данные в одном месте:")
print("Имя\t\tОценки\t\tСредний балл")
for name, row, avg in zip(students, grades, avg_per_student):
    print(f"{name}\t{row}\t{avg:.2f}")
