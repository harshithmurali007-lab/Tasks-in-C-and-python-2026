# Global variables to store student data
name = ""
roll_number = 0
marks = 0.0

# Function to enter student details
def enter_details():
    global name, roll_number, marks
    name = input("Enter Name: ")
    roll_number = int(input("Enter Roll Number: "))
    marks = float(input("Enter Marks: "))
    print("Details Saved!")

# Function to display student details
def display_details():
    print("\n--- Student Details ---")
    print(f"Name: {name}")
    print(f"Roll Number: {roll_number}")
    print(f"Marks: {marks}")

# Main loop
while True:
    print("\nPress 1 to Enter Details")
    print("Press 2 to Display Details")
    print("Press 3 to Exit")
    
    choice = input("Enter your choice: ")

    # Conditions to check user input
    if choice == '1':
        enter_details()
    elif choice == '2':
        display_details()
    elif choice == '3':
        print("Exiting program.")
        break
    else:
        print("Invalid choice! Please try again.")
