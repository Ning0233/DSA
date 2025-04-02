/*
This is a block style comment. Any text written inbetween the slash (/) and star (*) 
is ignored by the compiler. Comments are super useful for explaining what your program 
does to anyone who reads it.

^ You may delete the instructions above this line ^

Program Name: zhuang_ning_energy.c

Author: Ning Zhuang

Program Description: 
this is a program that takes user input of mass and height, it return a promt of time consumed, velocity of the object, energy produced.
*/

// This is an inline comment. Inline comments always start with the // symbol
// Any text that appears after the // is ignored.
// These are used to explain individual lines of code
// ^ You may delete these instructions ^

// Directives are always at the top of C programs
// These directives import the standard I/O and math libraries
# include <stdio.h>
# include <math.h>

// Every C program must contain a main() function
//call this file with -lm
int main(void) {
    float mass, height, time, velocity, energy; //Initialize the variables
	float gravity = 9.8;
	// here it takes float user inputs of mass and height
	printf("Enter the mass of the object in kilograms:");
	scanf("%f", &mass);
	printf("Enter the height of the drop in meters:");
	scanf("%f", &height);
	//here is the math calculation part that uses math module of c and returns 3 floats with name of time, velocity, and energy
	time = sqrt( 2 * (height/gravity));
	velocity = gravity * time;
	energy = (0.5 * mass) * pow(velocity, 2);
	printf("The time taken by an object weighing %f to reach the ground when dropped from a height of %f meters is %f seconds.\n", mass, height, time);
	printf("The velocity of the object when it hits the ground = %f m/s.\n", velocity);
	printf("The kinetic energy at the moment of impact with the ground is %f Joules.\n", energy);

	

		// Prints an informational message
	printf("This file is to help you get started on your first programs!\n");

    return 0;
}