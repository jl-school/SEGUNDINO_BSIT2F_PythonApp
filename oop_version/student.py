class Student:
    """Blueprint for a student: attributes (name, grades) and behaviors (methods)."""

    TERMS = ["prelim", "midterm", "prefinal", "final"]

    def __init__(self, name, grades=None):
        self.name = name
        self.grades = grades if grades is not None else {}

    def get_grades(self):
        """Ask for the grade of each term and store it in self.grades."""
        print()
        for term in self.TERMS:
            while True:
                try:
                    grade = float(input(f"Enter {term.capitalize()} Grade: "))
                    if 0 <= grade <= 100:
                        self.grades[term] = grade
                        break
                    print("Grade must be between 0 and 100.")
                except ValueError:
                    print("Incorrect Input. Please enter a proper grade.")

    def get_average(self):
        """Calculate the average of the student's grades."""
        return sum(self.grades.values()) / len(self.grades)

    def display(self):
        """Present the student's information."""
        print(f"\nHello {self.name}! Your average grade is {round(self.get_average()):.0f}\n")
