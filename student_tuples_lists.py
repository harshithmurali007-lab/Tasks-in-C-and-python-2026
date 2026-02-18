# List to store all student records
students = []

def add_student():
    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    usn = input("Enter USN: ")
    college = input("Enter College Name: ")

    # Store student details in a tuple
    student = (name, age, usn, college)

    # Add tuple to list
    students.append(student)

    print("Student details added successfully!\n")


def display_students():
    if len(students) == 0:
        print("No student records found.\n")
    else:
        print("\nStudent Details:")
        for i in range(len(students)):
            print("\nStudent", i + 1)
            print("Name:", students[i][0])
            print("Age:", students[i][1])
            print("USN:", students[i][2])
            print("College:", students[i][3])
        print()


# Menu driven program
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
