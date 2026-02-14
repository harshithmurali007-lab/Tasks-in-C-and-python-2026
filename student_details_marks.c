#include <stdio.h>

// Global variables to store student data
char name[50];
int roll_number;
float marks;

// Function to enter student details
void enter_details() {
    printf("Enter Name: ");
    scanf("%s", name);
    printf("Enter Roll Number: ");
    scanf("%d", &roll_number);
    printf("Enter Marks: ");
    scanf("%f", &marks);
    printf("Details Saved!\n");
}

// Function to display student details
void display_details() {
    printf("\n--- Student Details ---\n");
    printf("Name: %s\n", name);
    printf("Roll Number: %d\n", roll_number);
    printf("Marks: %.2f\n", marks);
}

int main() {
    int choice;

    // Loop to keep the program running
    while (1) {
        printf("\nPress 1 to Enter Details\n");
        printf("Press 2 to Display Details\n");
        printf("Press 3 to Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        // Conditions to check user input
        if (choice == 1) {
            enter_details();
        } else if (choice == 2) {
            display_details();
        } else if (choice == 3) {
            printf("Exiting program.\n");
            break;
        } else {
            printf("Invalid choice! Please try again.\n");
        }
    }

    return 0;
}
