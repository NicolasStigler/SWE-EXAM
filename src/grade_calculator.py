from src.student import Student
from src.policies import AttendancePolicy, ExtraPointsPolicy

class GradeCalculator:
    @staticmethod
    def calculate(student, has_reached_minimum_classes, all_years_teachers):
        if not isinstance(student, Student):
            raise TypeError("student must be an instance of the Student class.")

        total_weight = sum(e.weight for e in student.evaluations)
        if total_weight > 1:
            raise ValueError("The sum of the weights of the evaluations cannot be greater than 1.")

        weighted_average = sum(e.score * e.weight for e in student.evaluations)

        grade_after_attendance = AttendancePolicy.apply(weighted_average, has_reached_minimum_classes)
        final_grade = ExtraPointsPolicy.apply(grade_after_attendance, all_years_teachers)

        return {
            "weighted_average": weighted_average,
            "grade_after_attendance": grade_after_attendance,
            "final_grade": final_grade
        }
