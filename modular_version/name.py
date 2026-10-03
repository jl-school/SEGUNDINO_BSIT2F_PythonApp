def get_name():
    """Ask for the student's name."""
    while True:
        name = input("Enter Student Name: ").strip()
        if name:
            return name
        print("Name cannot be empty.")
