
from utils import generate_roll_number, current_datetime


class Student:
    def __init__(self, name, age):
        self.roll = generate_roll_number()  
        self.name = name
        self.age = age
        self.created_at = current_datetime() 

    def display(self):
        print("Roll Number:", self.roll)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Created At:", self.created_at)
