class Evaluation:
    def __init__(self, score, weight):
        if not (0 <= score <= 20):
            raise ValueError("Score must be between 0 and 20")
        if not (0 <= weight <= 1):
            raise ValueError("Weight must be between 0 and 1")
        self.score = score
        self.weight = weight
