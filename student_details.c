#include <stdio.h>

int main() {
    char name[100];
    char section[10];
    char college[100];
    int rollNumber;
    int semester;

    // Taking input
    printf("Enter Student Name: ");
    scanf(" %99[^\n]", name);   // Limit input to avoid overflow

    printf("Enter Roll Number: ");
    scanf("%d", &rollNumber);

    printf("Enter Section: ");
    scanf(" %9s", section);     // Limit input size

    printf("Enter Semester: ");
    scanf("%d", &semester);

    printf("Enter College Name: ");
    scanf(" %99[^\n]", college);  // Limit input size

    // Displaying output
    printf("\n--- Student Details ---\n");
    printf("Name        : %s\n", name);
    printf("Roll Number : %d\n", rollNumber);
    printf("Section     : %s\n", section);
    printf("Semester    : %d\n", semester);
    printf("College     : %s\n", college);

    return 0;
}
