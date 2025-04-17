#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>

#define BUFFER_SIZE 1024

int main() {
    char input[BUFFER_SIZE];
    char *args[BUFFER_SIZE / 2 + 1]; // Array to hold command and arguments

    while (1) {
        // Display the prompt
        printf("my_shell :> ");
        fflush(stdout);

        // Read input from the user
        if (fgets(input, BUFFER_SIZE, stdin) == NULL) {
            if (feof(stdin)) {
                // End-of-file (Ctrl+D) detected, exit gracefully
                printf("\nExiting my_shell.\n");
                break;
            } else {
                perror("Error reading input");
                continue;
            }
        }

        // Remove the newline character from the input
        input[strcspn(input, "\n")] = '\0';

        // Check if the user wants to exit
        if (strcmp(input, "exit") == 0) {
            printf("Exiting my_shell.\n");
            break;
        }

        // Parse the input into command and arguments
        int i = 0;
        char *token = strtok(input, " ");
        while (token != NULL) {
            args[i++] = token;
            token = strtok(NULL, " ");
        }
        args[i] = NULL; // Null-terminate the arguments array

        // Create a child process
        pid_t pid = fork();
        if (pid < 0) {
            perror("fork failed");
            continue;
        }

        if (pid == 0) {
            // Child process
            execvp(args[0], args);
            // If execvp fails, print an error and exit
            perror("execvp failed");
            exit(EXIT_FAILURE);
        } else {
            // Parent process
            int status;
            if (wait(&status) < 0) {
                perror("wait failed");
            }
        }
    }

    return 0;
}