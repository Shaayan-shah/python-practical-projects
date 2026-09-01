"""
Student Academic Performance Evaluator
Computes aggregate grades, GPA, percentage, and honors distribution
for student coursework marks.
"""

from typing import Dict, Tuple, Any


def calculate_grade(percentage: float) -> Tuple[str, float]:
    """Map percentage to Letter Grade and 4.0 GPA Scale."""
    if percentage >= 90:
        return "A+", 4.0
    elif percentage >= 80:
        return "A", 3.7
    elif percentage >= 70:
        return "B", 3.0
    elif percentage >= 60:
        return "C", 2.0
    elif percentage >= 50:
        return "D", 1.0
    else:
        return "F", 0.0


def evaluate_student(student_name: str, subjects_marks: Dict[str, float], total_per_subject: float = 100.0) -> Dict[str, Any]:
    """Generate comprehensive academic performance summary."""
    total_obtained = sum(subjects_marks.values())
    max_possible = len(subjects_marks) * total_per_subject
    percentage = (total_obtained / max_possible) * 100.0 if max_possible > 0 else 0.0
    grade, gpa = calculate_grade(percentage)

    return {
        "name": student_name,
        "obtained_marks": total_obtained,
        "max_marks": max_possible,
        "percentage": round(percentage, 2),
        "grade": grade,
        "gpa": gpa,
        "passed": grade != "F"
    }


def main():
    print("==================================================")
    print("      STUDENT ACADEMIC EVALUATOR & GPA SYSTEM     ")
    print("==================================================")

    student_name = input("Enter Student Name: ").strip() or "Student"
    subjects = ["Mathematics", "Computer Science", "Physics", "English", "Statistics"]
    marks: Dict[str, float] = {}

    print(f"\nEnter marks for {len(subjects)} subjects (out of 100):")
    for subj in subjects:
        while True:
            try:
                score = float(input(f"  - {subj}: ").strip())
                if 0 <= score <= 100:
                    marks[subj] = score
                    break
                print("    [Error] Marks must be between 0 and 100.")
            except ValueError:
                print("    [Error] Please enter a valid number.")

    summary = evaluate_student(student_name, marks)

    print("\n" + "=" * 50)
    print(f"             REPORT CARD - {summary['name'].upper()}")
    print("-" * 50)
    for subj, score in marks.items():
        print(f"  {subj:<20} : {score:>6.1f} / 100.0")
    print("-" * 50)
    print(f"  Total Obtained      : {summary['obtained_marks']:.1f} / {summary['max_marks']:.1f}")
    print(f"  Percentage          : {summary['percentage']:.2f}%")
    print(f"  Grade               : {summary['grade']}")
    print(f"  GPA (4.0 Scale)     : {summary['gpa']:.2f}")
    print(f"  Status              : {'PASSED [CONGRATULATIONS]' if summary['passed'] else 'NEEDS IMPROVEMENT'}")
    print("=" * 50 + "\n")


if __name__ == "__main__":
    main()
