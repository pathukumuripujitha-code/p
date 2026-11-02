

students = []
eligible = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nStudent", i + 1)

    name = input("Enter student name: ")
    aggregate = float(input("Enter aggregate marks: "))

    print("Enter marks in 3 subjects:")
    subjects = []
    for j in range(3):
        mark = float(input("Subject " + str(j + 1) + ": "))
        subjects.append(mark)

    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))

    student = [name, aggregate, attendance, income]

    if (aggregate >= 75 and
        min(subjects) >= 60 and
        attendance >= 75 and
        income <= 250000):

        eligible.append(student)
        print(name, "is eligible for scholarship")
    else:
        print(name, "is not eligible")

# Ranking based on marks, attendance and income
eligible.sort(key=lambda x: (-x[1], -x[2], x[3]))

print("\n===== SCHOLARSHIP RANKING =====")

if len(eligible) == 0:
    print("No eligible students found.")
else:
    for rank, student in enumerate(eligible, start=1):
        print("\nRank:", rank)
        print("Name:", student[0])
        print("Aggregate Marks:", student[1])
        print("Attendance:", student[2])
        print("Family Income:", student[3])


