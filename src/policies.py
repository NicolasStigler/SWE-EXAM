class AttendancePolicy:
    @staticmethod
    def apply(current_grade, has_reached_minimum_classes):
        if not has_reached_minimum_classes:
            return 0
        return current_grade

class ExtraPointsPolicy:
    @staticmethod
    def apply(current_grade, all_years_teachers):
        if all(all_years_teachers) and current_grade > 0:
            return min(20, current_grade + 1)
        return current_grade