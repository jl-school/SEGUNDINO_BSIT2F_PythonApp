from name import get_name
from grades import get_grades
from average import get_average
from display import get_print


def main():
    name = get_name()
    grades = get_grades()
    average = get_average(grades)
    get_print(name, average)


if __name__ == "__main__":
    main()
