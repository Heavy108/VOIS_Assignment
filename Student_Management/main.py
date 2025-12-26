
from student import Student
from marks import Marks
from attendance import Attendance
from fees import Fees
from report import Report
from utils import show_utilities, separator, print_header

import student as su

stu = Student("Amit", 20)
stu2 = Student("Riya", 19)
marks = Marks([85, 90, 88])
attendance = Attendance(45)
fees = Fees(25000)
print_header("STUDENT MANAGEMENT SYSTEM")


report = Report(stu, marks, attendance, fees)
report.generate()
separator()
show_utilities()
separator()

print("\nModule Name:", su.__name__)
# print("Module Dictionary:", student.__dict__)
print("Module file Name:", su.__file__)
separator()
