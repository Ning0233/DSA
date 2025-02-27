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
str1:  .string "Add result "   # String to use
str2:  .string "Sub result "   # String to use
str3:  .string "Not result "   # String to use
str4:  .string "Neg result "   # String to use
hexstr: .string "%x", 10       # String format to use (hex), followed by NL 
minus: .string "-"             # String for minus sign
equal: .string "="             # String for equal sign
newline: .string "\n"          # String for new line

int1:  .word 12    # Integer value 12
int2:  .word 5     # Integer value 5
int3:  .word 1000  # Integer value 1000
sum:   .word 0     # Variable to store the result

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
    sub x10, x9, x8   # x10 = x9 - x8 (int2 - int1)

    # Store the result in the "sum" variable
    la x7, sum        # Load the address of sum into x7
    sw x10, 0(x7)     # Store the value of x10 (the result) into the address of sum

    # Print the first operand (int2)
    la x7, int2       
    lw a0, 0(x7)      # Load the value of int2 into a0
    li a7, 1          # Syscall for print_int
    ecall

    # Print the "-" sign
    la a0, minus      
    li a7, 4          # Syscall for print_string
    ecall

    # Print the second operand (int1)
    la x7, int1       
    lw a0, 0(x7)      # Load the value of int1 into a0
    li a7, 1          # Syscall for print_int
    ecall

    # Print the "=" sign
    la a0, equal      
    li a7, 4          # Syscall for print_string
    ecall

    # Print the result (sum)
    la x7, sum        # Load the address of the sum
    lw a0, 0(x7)      # Load the sum into a0
    li a7, 1          # Syscall for print_int
    ecall

    # Print the new line character
    la a0, newline    
    li a7, 4          # Syscall for print_string
    ecall

    # Exit the program
    li a7, 10         # Syscall for exit
    ecall
