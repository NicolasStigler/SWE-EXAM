import unittest
from src.student import Student
from src.evaluation import Evaluation
from src.grade_calculator import GradeCalculator

class TestGradeCalculator(unittest.TestCase):

    def setUp(self):
        self.student = Student("U2021001")

    def test_should_calculate_final_grade_correctly_in_normal_case(self):
        self.student.add_evaluation(Evaluation(15, 0.3))
        self.student.add_evaluation(Evaluation(18, 0.4))
        self.student.add_evaluation(Evaluation(20, 0.3))
        result = GradeCalculator.calculate(self.student, True, [True])
        self.assertAlmostEqual(result["final_grade"], 18.7, places=2)

    def test_should_return_zero_when_minimum_attendance_is_not_met(self):
        self.student.add_evaluation(Evaluation(15, 0.5))
        self.student.add_evaluation(Evaluation(15, 0.5))
        result = GradeCalculator.calculate(self.student, False, [True])
        self.assertEqual(result["final_grade"], 0)

    def test_should_apply_extra_points_when_teachers_agree(self):
        self.student.add_evaluation(Evaluation(19, 1))
        result = GradeCalculator.calculate(self.student, True, [True])
        self.assertEqual(result["final_grade"], 20)

    def test_should_not_apply_extra_points_when_teachers_do_not_agree(self):
        self.student.add_evaluation(Evaluation(19, 1))
        result = GradeCalculator.calculate(self.student, True, [False])
        self.assertEqual(result["final_grade"], 19)

    def test_should_raise_error_when_total_weight_is_greater_than_one(self):
        with self.assertRaises(ValueError):
            self.student.add_evaluation(Evaluation(15, 0.6))
            self.student.add_evaluation(Evaluation(15, 0.5))
            GradeCalculator.calculate(self.student, True, [True])

    def test_should_handle_case_with_no_evaluations(self):
        result = GradeCalculator.calculate(self.student, True, [True])
        self.assertEqual(result["final_grade"], 0)

if __name__ == "__main__":
    unittest.main()