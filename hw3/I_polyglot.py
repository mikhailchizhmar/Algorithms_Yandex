n = int(input())
students = []
for i in range(n):
    m = int(input())
    students.append(set())
    for j in range(m):
        students[i].add(input())

at_least_one_student_know = set()
for stud in students:
    at_least_one_student_know |= stud

all_students_know = at_least_one_student_know.copy()
for stud in students:
    all_students_know &= stud

print(len(all_students_know))
for lang in all_students_know:
    print(lang)

print(len(at_least_one_student_know))
for lang in at_least_one_student_know:
    print(lang)


# быстрее можно вот так:
# students[0].intersection(*students[1:]),
# students[0].union(*students[1:])