#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <time.h>

#define FILENAME "unbuffered_output.txt"
#define STRING_TO_WRITE "This is a test string for unbuffered IO.\n"
#define NUM_WRITES 1000000

int main() {
    int fd = open(FILENAME, O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (fd == -1) {
        perror("open");
        return 1;
    }

    time_t start_time = time(NULL);

    for (int i = 0; i < NUM_WRITES; i++) {
        ssize_t bytes_written = write(fd, STRING_TO_WRITE, sizeof(STRING_TO_WRITE) - 1);
        if (bytes_written == -1) {
            perror("write");
            close(fd);
            return 1;
        }
        printf("%d: Called write(%d, str_to_write, %ld) which returned that %ld bytes were written\n", i, fd, sizeof(STRING_TO_WRITE) - 1, bytes_written);
    }

    time_t end_time = time(NULL);
    printf("Time elapsed: %ld seconds\n", end_time - start_time);

    close(fd);
    return 0;
}