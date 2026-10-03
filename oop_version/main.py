from student import Student


def main():
    name = input("Enter Student Name: ").strip()
    student1 = Student(name)      # create an object (instance) of the class
    student1.get_grades()
    student1.display()


if __name__ == "__main__":
    main()
