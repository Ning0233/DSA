/*
This is a block style comment. Any text written inbetween the slash (/) and star (*) 
is ignored by the compiler. Comments are super useful for explaining what your program 
does to anyone who reads it.

^ You may delete the instructions above this line ^

Program Name: ning_zhuang_passenger.c

Author: Ning Zhuang

Program Description:
[Program Description Goes Here]
*/

// This is an inline comment. Inline comments always start with the // symbol
// Any text that appears after the // is ignored.
// These are used to explain individual lines of code
// ^ You may delete these instructions ^

// Directives are always at the top of C programs
// These directives import the standard I/O and math libraries
# include <stdio.h>
# include <math.h>

// Use macro directives to declare constants for all string lengths
# define Name_LEN 16
# define AIRLINE_LEN 32
# define FLIGHT_NUM_LEN 8
# define SEAT_ROW_LEN 4
# define SEAT_LETTER_LEN 2
// Every C program must contain a main() function
int main(void) {

	// declare varibales
	char first_name[Name_LEN];
	char last_name[Name_LEN];
	char airline[AIRLINE_LEN];
	char flight_number[FLIGHT_NUM_LEN];
	char seat_row[SEAT_ROW_LEN];
	char seat_letter[SEAT_LETTER_LEN];
	
	// promt user input
	printf("Enter the passenger’s first name: ");
	scanf("%15s", first_name);
	printf("Enter the passenger’s last name: ");
	scanf("%15s", last_name);
	printf("Enter the airline name: ");
	scanf("%31s", airline);
	printf("Enter the flight number: ");
	scanf("%7s", flight_number);
	printf("Enter the seat row number:");
	scanf("%3s", seat_row);
	printf("Enter the seat letter:");
	scanf("%1s", seat_letter);

	//print
	printf("Welcome %s %s! Your flight is %s %s. Your seat is %s%s\n", first_name, last_name, airline, flight_number, seat_row, seat_letter);

    return 0;
}