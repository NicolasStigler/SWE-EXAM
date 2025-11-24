from src.student import Student
from src.evaluation import Evaluation
from src.grade_calculator import GradeCalculator

def main():
    print("Welcome to the UTEC Grade Calculator")

    student_id = input("Enter the student's ID: ")
    student = Student(student_id)

    num_evaluations = int(input("Enter the number of evaluations: "))
    for i in range(num_evaluations):
        score = float(input(f"Enter the score for evaluation {i + 1}: "))
        weight = float(input(f"Enter the weight for evaluation {i + 1} (as a decimal): "))
        student.add_evaluation(Evaluation(score, weight))

    has_reached_minimum_classes_input = input("Has the student reached the minimum required classes? (yes/no): ")
    has_reached_minimum_classes = has_reached_minimum_classes_input.lower() == 'yes'

    all_years_teachers_input = input("Are all teachers in agreement to award extra points? (yes/no): ")
    all_years_teachers = all_years_teachers_input.lower() == 'yes'

    calculation_result = GradeCalculator.calculate(student, has_reached_minimum_classes, [all_years_teachers])

    print("\n--- Calculation Details ---")
    print(f"Weighted Average: {calculation_result['weighted_average']:.2f}")
    if not has_reached_minimum_classes:
        print("Penalty for not meeting minimum attendance applied.")
    print(f"Grade after attendance policy: {calculation_result['grade_after_attendance']:.2f}")
    if all_years_teachers:
        print("Extra points awarded.")
    print(f"Final Grade: {calculation_result['final_grade']:.2f}")

if __name__ == "__main__":
    main()