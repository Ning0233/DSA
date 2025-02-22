#include <stdio.h>
#include <time.h>
#include <string.h>

#define FILENAME "buffered_output.txt"
#define STRING_TO_WRITE "This is a test string for buffered IO.\n"
#define NUM_WRITES 1000000

int main() {
    FILE *file = fopen(FILENAME, "w");
    if (file == NULL) {
        perror("fopen");
        return 1;
    }

    time_t start_time = time(NULL);
    size_t str_len = strlen(STRING_TO_WRITE);

    for (int i = 0; i < NUM_WRITES; i++) {
        int result = fprintf(file, "%s", STRING_TO_WRITE);
        if (result < 0) {
            perror("fprintf");
            fclose(file);
            return 1;
        }
        // Simulate the expected output format
        printf("%d: Called fprintf (my_file,\"%%s\\n\", str to write); which returned that %d characters written\n", i, result);
    }

    time_t end_time = time(NULL);
    printf("Time elapsed: %ld seconds\n", end_time - start_time);

    fclose(file);
    return 0;
}