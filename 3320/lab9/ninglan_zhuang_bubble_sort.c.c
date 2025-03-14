#include <stdio.h>

void bubble_sort(int array[], int n, int *min, int *max) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1 - i; j++) {
            if (array[j] > array[j + 1]) {
                // Swap the elements
                int temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
            }
        }
    }
    // Assign the min and max values
    *min = array[0];
    *max = array[n - 1];
}

int main() {
    int array[10];
    int min, max;

    // Prompt the user to enter 10 integers
    for (int i = 0; i < 10; i++) {
        printf("Enter integer %d: ", i+1);
        scanf("%d", &array[i]);
    }


    // Call the bubble_sort function
    bubble_sort(array, 10, &min, &max);

    // Output the sorted list
    printf("Sorted list: [");
    for (int i = 0; i < 10; i++) {
        printf("%d", array[i]);
    }
    printf("]\n");
    // Output the min and max values
    printf("Min: %d\n", min);
    printf("Max: %d\n", max);

    return 0;
}