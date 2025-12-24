students = {
    "Amit": [85, 90, 88],
    "Neha": [72, 78, 75],
    "Rahul": [60, 65, 70],
    "Priya": [92, 95, 94],
    "Karan": [55, 58, 50],
}


def calculate_average(marks):
    return sum(marks) / len(marks)


def assign_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "Fail"


top_student = ""
top_average = 0
print("Student Results:\n")

for name, marks in students.items():
    
    average = calculate_average(marks)
    grade = assign_grade(average)

    print(f"Name: {name}, Average: {average:.2f}, Grade: {grade}")

    if average > top_average:
        top_average = average
        top_student = name

print("\nTop Scorer:")
print(f"Name: {top_student}, Average Marks: {top_average:.2f}")
