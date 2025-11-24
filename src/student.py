from src.evaluation import Evaluation

MAX_EVALUATIONS = 10

class Student:
    def __init__(self, student_id):
        self.student_id = student_id
        self.evaluations = []

    def add_evaluation(self, evaluation):
        if len(self.evaluations) >= MAX_EVALUATIONS:
            raise ValueError(f"Maximum number of evaluations ({MAX_EVALUATIONS}) reached.")
        if not isinstance(evaluation, Evaluation):
            raise TypeError("The evaluation must be an instance of the Evaluation class.")
        self.evaluations.append(evaluation)
