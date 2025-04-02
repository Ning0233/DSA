.data
    str1:       .string "Enter a char: "
    str2:       .string "Enter an int: "
    str3:       .string "Enter a string: "
    chars_read: .string "Number of chars read is: "
    newline:    .byte 10, 0
    mychar:     .byte 0
    int1:       .word 0
    .equ BUFFER_SIZE, 100
    mybuffer:   .space BUFFER_SIZE
    temp:       .word 0

.text
.globl main

main:
    # Prompt and read a character
    la a0, str1
    li a7, 4          # Print string syscall
    ecall

    li a7, 12         # Read character syscall
    ecall
    la t0, mychar
    sb a0, 0(t0)      # Store the character

    # Prompt and read an integer
    la a0, str2
    li a7, 4          # Print string syscall
    ecall

    li a7, 5          # Read integer syscall
    ecall
    la t0, int1
    sw a0, 0(t0)      # Store the integer

read_again:
    # Prompt and read a string
    la a0, str3
    li a7, 4          # Print string syscall
    ecall

    li a7, 63         # Read string syscall
    li a0, 0          # File descriptor (STDIN)
    la a1, mybuffer   # Buffer address
    li a2, BUFFER_SIZE
    ecall

    mv s0, a0         # Save number of chars read
    beq a0, x0, eof_reached # If 0 chars read, EOF reached

    # Print number of chars read
    la a0, chars_read
    li a7, 4          # Print string syscall
    ecall

    mv a0, s0         # Move number of chars read to a0
    li a7, 1          # Print integer syscall
    ecall

    la a0, newline
    li a7, 4          # Print newline
    ecall

    j read_again      # Loop to read again

eof_reached:
    # Exit program
    li a7, 10         # Exit syscall
    ecall
