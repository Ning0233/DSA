#include <stdio.h>

int main() {
    int age = 25;
    int voteage = 18;
    if (age >= voteage) {
        printf("Old enough to vote");
    } else {
        printf("Not old enough");
    };
    return 0;
}