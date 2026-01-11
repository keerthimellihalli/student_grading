# Program to calculate student grade
import sys

def calculate_average(m1, m2, m3):
    return (m1 + m2 + m3) / 3

def assign_grade(avg):
    if avg >= 90:
        return "S"
    elif avg >= 80:
        return "A"
    elif avg >= 65:
        return "B"
    elif avg >= 50:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"

if __name__ == "__main__":
    print("=== Student Grade Calculator ===")

    # Jenkins-safe default values
    name = "Test Student"
    department = "BCA"
    semester = 5
    m1, m2, m3 = 85, 78, 90

    print("\n--- Program Parameters ---")
    print(f"Student Name : {name}")
    print(f"Department   : {department}")
    print(f"Semester     : {semester}")
    print(f"Marks        : {m1}, {m2}, {m3}")

    average = calculate_average(m1, m2, m3)
    grade = assign_grade(average)

    print(f"\nAverage : {average:.2f}")
    print(f"Grade   : {grade}")
