# This code is based on:
#   https://smist08.wordpress.com/2024/10/21/risc-v-on-the-raspberry-pi-pico-2/
#   Stephen Smith, October 21, 2024
# It is supposed to print a string, then the count of how many times it has
# executed the loop. However, the integer printing does not work as expected.
#
# Another source:
#   https://github.com/kvakil/venus/wiki/Environmental-Calls
#   Keyhan Vakil, Aug 13, 2017
# shows the ecalls (environmental calls, like software interrupts)
#
# Combining these two, the code below works.
# -MCW
.data   
str1:   .string "Add result "   # String to use for addition (kept for reference)
str2:   .string "Sub result "   # String to use for subtraction
str3:   .string "Not result "   # String to use
str4:   .string "Neg result "   # String to use
hexstr: .string "%x", 10        # String format to use (hex), followed by NL 

int1: .word 12    # Integer value 12
int2: .word 5     # Integer value 5
int3: .word 1000  # Integer value 1000
sum:  .word 0     # Variable to store the result

.text
.globl _start

_start:
    # Load the address of int1 into x7
    la x7, int1       

    # Load the value at the address of int1 into x8
    lw x8, 0(x7)      # x8 = *int1

    # Load the address of int2 into x7
    la x7, int2       

    # Load the value at the address of int2 into x9
    lw x9, 0(x7)      # x9 = *int2

    # Perform the subtraction and store the result in x10
    sub x10, x8, x9   # x10 = x8 - x9 (12 - 5)

    # Store the result in the "sum" variable
    la x7, sum        # Load the address of sum into x7
    sw x10, 0(x7)     # Store the value of x10 (the result) into the address of sum

    # Print "Sub result "
    la a0, str2       # Load the address of "Sub result " into a0
    li a7, 4          # Syscall for print_string (update this to the correct syscall number for your environment)
    ecall

    # Print the result (sum)
    la x7, sum        # Load the address of the sum
    lw a0, 0(x7)      # Load the sum into a0
    li a7, 1          # Syscall for print_int (update this to the correct syscall number for your environment)
    ecall

    # Perform the NOT operation on the value of int1 and store the result in x11
    la x7, int1       # Load the address of int1 into x7
    lw x8, 0(x7)      # Load the value at the address of int1 into x8
    not x11, x8       # Perform NOT operation on x8 and store the result in x11

    # Store the result in the "sum" variable
    la x7, sum        # Load the address of sum into x7
    sw x11, 0(x7)     # Store the value of x11 (the result) into the address of sum

    # Print "Not result "
    la a0, str3       # Load the address of "Not result " into a0
    li a7, 4          # Syscall for print_string (update this to the correct syscall number for your environment)
    ecall

    # Print the result (sum)
    la x7, sum        # Load the address of the sum
    lw a0, 0(x7)      # Load the sum into a0
    li a7, 1          # Syscall for print_int (update this to the correct syscall number for your environment)
    ecall

    # Exit the program
    li a7, 10         # Syscall for exit (update this to the correct syscall number for your environment)
    ecall
