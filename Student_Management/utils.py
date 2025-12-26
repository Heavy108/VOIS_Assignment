import math
import random
from datetime import datetime

def separator():
    print("-" * 30)

def show_utilities():
    print("Random ID:", random.randint(1000, 9999))
    print("Rounded Value:", math.ceil(92.3))
    print("Current Date:", datetime.now())

_roll_counter = 10  


def generate_roll_number():
    global _roll_counter
    _roll_counter += 1
    return _roll_counter


def generate_random_id():
    return random.randint(1000, 9999)


def current_datetime():
    return datetime.now()

def print_header(title):
    separator()
    print(title)
    print("=" * 30)


def validate_marks(marks):
    for m in marks:
        if m < 0 or m > 100:
            return False
    return True


def grade_from_average(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"
