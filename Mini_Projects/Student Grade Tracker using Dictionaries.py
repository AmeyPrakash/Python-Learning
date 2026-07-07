students = {}
num_students = int(input("Enter the number of students: "))
for _ in range(num_students):
    name = input("Enter student name: ")
    num_students = int(input(f"Enter the number of subjects for {name}: "))

    marks = {}

    for _ in range (num_students):
        subjects = input("Enter subject name: ")
        score = float(input(f"Enter marks for {subjects}: "))
        marks[subjects] = score
    total = sum(marks.values())
    average = total / len(marks)
    
    students[name] = {
        "marks": marks,
        "total": total,
        "average": round(average, 2)
    }        

print("\nStudents Grade Report: ")
for name, info in students.items():
    print(f"\nName: {name}")
    for subject, score in info["marks"].items():
        print(f" {subject}: {score}")
    print(f"Total : {info['total']}")
    print(f"Average: {info['average']}")