#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#define ALPHABET_SIZE 26

int main() {
    FILE *file = fopen("sample.txt", "r");
    if (file == NULL) {
        perror("Error opening file");
        return EXIT_FAILURE;
    }

    int frequency[ALPHABET_SIZE] = {0};
    char ch;

    while ((ch = fgetc(file)) != EOF) {
        if (isalpha(ch)) {
            ch = tolower(ch);
            frequency[ch - 'a']++;
        }
    }

    fclose(file);

    int max_freq = 0;
    char most_freq_char = 'a';
    for (int i = 0; i < ALPHABET_SIZE; i++) {
        if (frequency[i] > max_freq) {
            max_freq = frequency[i];
            most_freq_char = 'a' + i;
        }
    }

    printf("The most frequent letter is '%c' with a count of %d\n", most_freq_char, max_freq);

    return EXIT_SUCCESS;
}