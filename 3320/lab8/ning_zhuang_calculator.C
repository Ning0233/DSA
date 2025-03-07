#include <stdio.h>
#include <math.h>

// Function declarations
float addition(float left, float right);
float subtraction(float left, float right);
float multiplication(float left, float right);
float division(float left, float right);
float power(float left, float right);
float floor_division(float left, float right);

int main() {
    float left, right, result;
    char op[3];

    // Prompt user for input
    printf("Enter an expression (e.g., 3.5 + 4.2): ");
    scanf("%f %2s %f", &left, op, &right);

    // Determine the operator and call the corresponding function
    if (op[0] == '+' && op[1] == '\0') {
        result = addition(left, right);
    } else if (op[0] == '-' && op[1] == '\0') {
        result = subtraction(left, right);
    } else if (op[0] == '*' && op[1] == '\0') {
        result = multiplication(left, right);
    } else if (op[0] == '/' && op[1] == '\0') {
        result = division(left, right);
    } else if (op[0] == '*' && op[1] == '*') {
        result = power(left, right);
    } else if (op[0] == '/' && op[1] == '/') {
        result = floor_division(left, right);
    } else {
        printf("Error: Invalid operator\n");
        return 1;
    }

    // Output the result
    printf("Result: %f\n", result);
    return 0;
}

// Function definitions
float addition(float left, float right) {
    return left + right;
}

float subtraction(float left, float right) {
    return left - right;
}

float multiplication(float left, float right) {
    return left * right;
}

float division(float left, float right) {
    return left / right;
}

float power(float left, float right) {
    return pow(left, right);
}

float floor_division(float left, float right) {
    return floor(left / right);
}
