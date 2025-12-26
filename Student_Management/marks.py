from utils import validate_marks


class Marks:
    def __init__(self, marks):
        if not validate_marks(marks):
            raise ValueError("Invalid marks! Marks must be between 0 and 100.")
        self.marks = marks

    def average(self):
        return sum(self.marks) / len(self.marks)
