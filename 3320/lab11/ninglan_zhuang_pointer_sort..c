#include <stdio.h>

void bubble_sort(int array[], int n, int *min, int *max) {
    for (int i = 0; i < n - 1; i++) {
        for (int *ptr = array; ptr < array + n - 1 - i; ptr++) {
            if (*ptr > *(ptr + 1)) {
                // Swap the elements using pointers
                int temp = *ptr;
                *ptr = *(ptr + 1);
                *(ptr + 1) = temp;
            }
        }
    }
    // Assign the min and max values
    *min = *array;          // First element (smallest after sorting)
    *max = *(array + n - 1); // Last element (largest after sorting)
}

int main() {
    int array[10];
    int min, max;

    // Prompt the user to enter 10 integers
    for (int i = 0; i < 10; i++) {
        printf("Enter integer %d: ", i + 1);
        scanf("%d", &array[i]);
    }

    // Call the bubble_sort function
    bubble_sort(array, 10, &min, &max);

    // Output the sorted list
    printf("Sorted list: [");
    for (int *ptr = array; ptr < array + 10; ptr++) {
        printf("%d", *ptr);
        if (ptr < array + 9) {
            printf(", ");
        }
    }
    printf("]\n");

    // Output the min and max values
    printf("Largest: %d\n", min);
    printf("Smallest: %d\n", max);

    return 0;
}