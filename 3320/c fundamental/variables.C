#include <stdio.h>

int main() {
	// Declare a varible	
	int myNum = 15;
	float myFloat = 5.99;
	char myLetter = 'D';
	// Assign a value to variable
	int v2;
	v2 = 20;
	printf("%d", myNum);
	printf("%f", myFloat);
	printf("%c", myLetter);
	int x = 5, y = 6, z = 50;
	printf("\n%d\n", x + y + z );
	int studentID = 15, studentAge = 23;
	float studentFee = 75.25;
	char StudentGrade = 'B';
	printf("Student ID is: %d\n", studentID);
	printf("Student age is: %d\n", studentAge);
	printf("Student fee is: %f\n", studentFee);
	printf("Student grade is: %c\n", StudentGrade);

	int length = 10, width = 5;
	int area;

	area = length * width / 2;
	printf("area of triangle is are %d", area);
	return 0;

}

