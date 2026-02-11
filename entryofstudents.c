#include <stdio.h>

int main() {
    char name[5][50];   // 2D array for 5 names
    int age[5];
    float marks[5];

    // Input details
    for(int i = 0; i < 5; i++) {
        printf("\nEnter details for Student %d\n", i + 1);

        printf("Name: ");
        scanf(" %[^\n]", name[i]);   // Allows spaces in name

        printf("Age: ");
        scanf("%d", &age[i]);

        printf("Marks: ");
        scanf("%f", &marks[i]);
    }

    // Display details
    printf("\n----- Student Details -----\n");

    for(int i = 0; i < 5; i++) {
        printf("\nStudent %d:\n", i + 1);
        printf("Name: %s\n", name[i]);
        printf("Age: %d\n", age[i]);
        printf("Marks: %.2f\n", marks[i]);
    }

    return 0;
}
