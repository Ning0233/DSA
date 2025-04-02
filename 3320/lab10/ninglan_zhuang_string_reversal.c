#include <stdio.h>
#include <string.h>

// Function prototypes
void reverseString(char *str);
void swap(char *left, char *right);

int main() {
    // Declare a character array to store the user's input
    char input[100]; // Adjust size as needed for maximum string length

    // Prompt the user to enter a string
    printf("Enter a string: ");
    if (fgets(input, sizeof(input), stdin) != NULL) {
        // Remove the newline character if present
        size_t len = strlen(input);
        if (len > 0 && input[len - 1] == '\n') {
            input[len - 1] = '\0';
        }

        printf("Original string: %s\n", input);
        
        // Call reverseString to reverse the input string
        reverseString(input);

        // Print the reversed string
        printf("Reversed string: %s\n", input);
    } else {
        printf("Error reading input.\n");
    }

    return 0;
}

// Function to reverse a string in-place
void reverseString(char *str) {
    int left = 0;
    int right = strlen(str) - 1;

    // Swap characters from the beginning and end towards the middle
    while (left < right) {
        swap(&str[left], &str[right]);
        left++;
        right--;
    }
}

// Helper function to swap two characters
void swap(char *left, char *right) {
    char temp = *left;
    *left = *right;
    *right = temp;
}