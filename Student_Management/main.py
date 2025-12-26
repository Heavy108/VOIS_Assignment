from student import Student
from marks import Marks
from attendance import Attendance
from fees import Fees
from report import Report
from utils import show_utilities, separator, print_header

import student as su

print_header("STUDENT MANAGEMENT SYSTEM")

stu1 = Student("Amit", 20)
marks1 = Marks([85, 90, 88])
attendance1 = Attendance(45)
fees1 = Fees(25000)

report1 = Report(stu1, marks1, attendance1, fees1)
report1.generate()
separator()

stu2 = Student("Riya", 19)
marks2 = Marks([78, 82, 80])
attendance2 = Attendance(42)
fees2 = Fees(23000)

report2 = Report(stu2, marks2, attendance2, fees2)
report2.generate()
separator()

show_utilities()
separator()

print("Module Name:", su.__name__)
print("Module File Name:", su.__file__)
separator()
