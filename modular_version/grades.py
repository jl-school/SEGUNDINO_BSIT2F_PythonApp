TERMS = ["prelim", "midterm", "prefinal", "final"]


def get_grades():
    """Ask for the grade of each term and return them as a dictionary."""
    grades = {}
    print()
    for term in TERMS:
        while True:
            try:
                grade = float(input(f"Enter {term.capitalize()} Grade: "))
                if 0 <= grade <= 100:
                    grades[term] = grade
                    break
                print("Grade must be between 0 and 100.")
            except ValueError:
                print("Incorrect Input. Please enter a proper grade.")
    return grades
