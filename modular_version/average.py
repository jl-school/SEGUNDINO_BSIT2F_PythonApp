def get_average(grades):
    """Calculate the average of all term grades."""
    total = 0
    for grade in grades.values():
        total += grade
    return total / len(grades)
