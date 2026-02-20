# List to store all student records
students = []

def add_student():
    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    section = input("Enter Section: ")
    usn = input("Enter USN: ")
    college = input("Enter College Name: ")

    # Tuple for basic details
    basic_info = (name, age)

    # Dictionary for full details
    student = {
        "Basic Info": basic_info,
        "Section": section,
        "USN": usn,
        "College": college
    }

    # Add dictionary to list
    students.append(student)

    print("Student details added successfully!\n")


def display_students():
    if len(students) == 0:
        print("No student records found.\n")
    else:
        print("\nStudent Details:")
        for i, student in enumerate(students, start=1):
            print(f"\nStudent {i}")
            print("Name:", student["Basic Info"][0])
            print("Age:", student["Basic Info"][1])
            print("Section:", student["Section"])
            print("USN:", student["USN"])
            print("College:", student["College"])
        print()


# Menu Driven Program
while True:
    print("1. Add Student")
    print("2. Display Students")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        display_students()
    elif choice == 3:
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.\n")