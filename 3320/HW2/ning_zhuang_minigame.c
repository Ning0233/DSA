/*
 * Author: Ning Zhuang
 o
 * Program: Guessing Minigame
 * Description: This program implements a guessing minigame where the user must guess a randomly 
 *              generated 4-digit code within a limited number of attempts. The program provides 
 *              feedback on the user's guesses, including how many digits are correct and in the 
 *              correct position, and how many digits are correct but in the wrong position. 
 *              The user can quit the game at any time by entering 'q' or 'Q'.
 */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <ctype.h>
#include <string.h>

#define TRIES 10
#define DIGITS 4
#define RANGE 9

// Function to generate a random code
void generate_code(int code[]) {
    for (int i = 0; i < DIGITS; i++) {
        code[i] = rand() % (RANGE + 1);
    }
}

// Function to check the player's guess
void check_guess(int code[], int guess[], int *correct_pos, int *correct_digit) {
    int code_used[DIGITS] = {0};
    int guess_used[DIGITS] = {0};

    *correct_pos = 0;
    *correct_digit = 0;

    // Check for digits in the correct position
    for (int i = 0; i < DIGITS; i++) {
        if (guess[i] == code[i]) {
            (*correct_pos)++;
            code_used[i] = 1;
            guess_used[i] = 1;
        }
    }

    // Check for correct digits in the wrong position
    for (int i = 0; i < DIGITS; i++) {
        if (!guess_used[i]) {
            for (int j = 0; j < DIGITS; j++) {
                if (!code_used[j] && guess[i] == code[j]) {
                    (*correct_digit)++;
                    code_used[j] = 1;
                    break;
                }
            }
        }
    }
}

int main() {
    int code[DIGITS];
    int guess[DIGITS];
    char input[20];
    int attempts = 0;
    int correct_pos, correct_digit;

    // Seed the random number generator
    srand(time(NULL));

    // Generate the random code
    generate_code(code);

    printf("Welcome to the Guessing Minigame!\n");
    printf("You need to guess a %d-digit code. Each digit is between 0 and %d.\n", DIGITS, RANGE);
    printf("You have %d attempts. Enter 'q' or 'Q' to quit.\n\n", TRIES);

    while (attempts < TRIES) {
        printf("Attempt %d/%d: Enter your %d-digit guess: ", attempts + 1, TRIES, DIGITS);
        scanf("%s", input);

        // Check if the user wants to quit
        if (tolower(input[0]) == 'q') {
            printf("You quit the game. Better luck next time!\n");
            return 0;
        }

        // Validate input length
        if (strlen(input) != DIGITS) {
            printf("Invalid input. Please enter exactly %d digits.\n", DIGITS);
            continue;
        }

        // Convert input to integers
        for (int i = 0; i < DIGITS; i++) {
            if (!isdigit(input[i])) {
                printf("Invalid input. Please enter only digits.\n");
                goto next_attempt;
            }
            guess[i] = input[i] - '0';
        }

        // Check the guess
        check_guess(code, guess, &correct_pos, &correct_digit);

        if (correct_pos == DIGITS) {
            printf("Congratulations! You guessed the code correctly!\n");
            return 0;
        }

        printf("Feedback: %d digit(s) correct and in the correct position, %d digit(s) correct but in the wrong position.\n", correct_pos, correct_digit);

        if (guess[0] < code[0]) {
            printf("Hint: The code is higher than your guess.\n");
        } else {
            printf("Hint: The code is lower than your guess.\n");
        }

    next_attempt:
        attempts++;
    }

    // If the player runs out of attempts
    printf("You've used all your attempts. The correct code was: ");
    for (int i = 0; i < DIGITS; i++) {
        printf("%d", code[i]);
    }
    printf("\nBetter luck next time!\n");

    return 0;
}