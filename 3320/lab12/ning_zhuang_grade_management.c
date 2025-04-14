#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Define the Student structure
typedef struct {
    char name[50];
    int studentID;
    float grades[5];
    float avgGrade;
    char letterGrade;
} Student;

// Define the Course structure
typedef struct {
    int courseNum;
    char courseName[50];
    Student *roster;
} Course;

// Function to calculate the letter grade
char calculate_letter_grade(float avg) {
    if (avg >= 90) return 'A';
    if (avg >= 80) return 'B';
    if (avg >= 70) return 'C';
    if (avg >= 60) return 'D';
    return 'F';
}

// Function to input student data
void input_student_data(Student *student, int studentIndex) {
    printf("Enter details for Student %d:\n", studentIndex + 1);
    printf("Name: ");
    scanf(" %[^\n]", student->name);
    printf("Student ID: ");
    scanf("%d", &student->studentID);

    float total = 0;
    for (int i = 0; i < 5; i++) {
        do {
            printf("Enter grade for Assignment %d (0-100): ", i + 1);
            scanf("%f", &student->grades[i]);
            if (student->grades[i] < 0 || student->grades[i] > 100) {
                printf("Invalid grade. Please enter a value between 0 and 100.\n");
            }
        } while (student->grades[i] < 0 || student->grades[i] > 100);
        total += student->grades[i];
    }

    student->avgGrade = total / 5.0;
    student->letterGrade = calculate_letter_grade(student->avgGrade);
}

// Function to display the class roster and grades
void display_class_roster(Course *course, int classSize) {
    printf("\nClass Roster for Course: %s (Course Number: %d)\n", course->courseName, course->courseNum);
    printf("--------------------------------------------------------------------------------\n");
    printf("| %-20s | %-10s | %-30s | %-10s | %-10s |\n", "Name", "Student ID", "Grades", "Avg Grade", "Letter");
    printf("--------------------------------------------------------------------------------\n");

    for (int i = 0; i < classSize; i++) {
        Student *student = &course->roster[i];
        printf("| %-20s | %-10d | ", student->name, student->studentID);
        for (int j = 0; j < 5; j++) {
            printf("%.1f ", student->grades[j]);
        }
        printf("| %-10.2f | %-10c |\n", student->avgGrade, student->letterGrade);
    }
    printf("--------------------------------------------------------------------------------\n");
}

int main() {
    Course course;

    // Input course details
    printf("Enter the course number: ");
    scanf("%d", &course.courseNum);
    printf("Enter the course name: ");
    scanf(" %[^\n]", course.courseName);

    // Input class size
    int classSize;
    printf("Enter the total number of students in the class: ");
    scanf("%d", &classSize);

    // Dynamically allocate memory for the roster
    course.roster = (Student *)malloc(classSize * sizeof(Student));
    if (course.roster == NULL) {
        printf("Memory allocation failed. Exiting program.\n");
        return 1;
    }

    // Input data for each student
    for (int i = 0; i < classSize; i++) {
        input_student_data(&course.roster[i], i);
    }

    // Display the class roster and grades
    display_class_roster(&course, classSize);

    // Free allocated memory
    free(course.roster);

    return 0;
}