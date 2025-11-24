# CS-GradeCalculator Diagrama de Clases UML

Este diagrama muestra las relaciones entre las clases principales en el sistema CS-GradeCalculator.

```mermaid
classDiagram
    class Student {
        +String student_id
        +List~Evaluation~ evaluations
        +add_evaluation(evaluation: Evaluation)
    }

    class Evaluation {
        +float score
        +float weight
    }

    class GradeCalculator {
        <<static>>
        +calculate(student: Student, has_reached_minimum_classes: bool, all_years_teachers: List~bool~) dict
    }

    class AttendancePolicy {
        <<static>>
        +apply(current_grade: float, has_reached_minimum_classes: bool) float
    }

    class ExtraPointsPolicy {
        <<static>>
        +apply(current_grade: float, all_years_teachers: List~bool~) float
    }

    Student "1" o-- "0..10" Evaluation
    GradeCalculator ..> Student
    GradeCalculator ..> AttendancePolicy
    GradeCalculator ..> ExtraPointsPolicy
```

### Relaciones Explicadas:

*   **`Student` o-- `Evaluation`**: Un objeto `Student` puede contener entre 0 y 10 objetos `Evaluation` (Composición).
*   **`GradeCalculator` ..> `Student`**: La clase `GradeCalculator` depende de la clase `Student` para acceder a las evaluaciones del estudiante.
*   **`GradeCalculator` ..> `AttendancePolicy`**: La `GradeCalculator` utiliza la `AttendancePolicy` para aplicar las reglas de asistencia.
*   **`GradeCalculator` ..> `ExtraPointsPolicy`**: La `GradeCalculator` utiliza la `ExtraPointsPolicy` para aplicar las reglas de puntos adicionales.