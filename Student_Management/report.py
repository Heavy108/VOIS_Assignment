from utils import print_header,grade_from_average
class Report:
    def __init__(self, student, marks, attendance, fees):
        self.student = student
        self.marks = marks
        self.attendance = attendance
        self.fees = fees

    def generate(self):
        print_header("STUDENT REPORT")
        self.student.display()
        avg = self.marks.average()
        print("Average Marks:", avg)
        print("Grade:", grade_from_average(avg))
        print("Attendance:", self.attendance.days_present, "days")
        print("Fees Paid:", self.fees.amount)