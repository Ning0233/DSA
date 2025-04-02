.data
    str1:       .string "Enter a char: "
    str2:       .string "Enter an int: "
    str3:       .string "Enter a string: "
    chars_read: .string "Number of chars read is: "
    string_read: .string "String read is: !"
    int_read:   .string "Int value read is: !"
    char_read:  .string "Char value read is: !"
    newline:    .byte 10, 0        # Newline character (ASCII 10)
    exclamation: .byte 33, 0       # ASCII for '!'
    mychar:     .byte 0
    int1:       .word 0
    BUFFER_SIZE: .word 100        # Define BUFFER_SIZE as a word (100 bytes)
    mybuffer:   .space 100        # Allocate space for buffer (100 bytes)
    temp:       .word 0
    NL:         .byte 10          # Newline character (single byte)

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
    # Prompt and read a string (SIMPLE_READ)
    la a0, str3
    li a7, 4          # Print string syscall
    ecall

    li a7, 63         # Read string syscall (SIMPLE_READ)
    li a0, 0          # File descriptor (STDIN)
    la a1, mybuffer   # Buffer address
    li a2, 100        # Number of bytes to read
    ecall

    mv s0, a0         # Save number of chars read
    beq a0, x0, eof_reached # If 0 chars read, EOF reached

    # Check for newline character and remove it if present
    la t0, mybuffer   # Load buffer address
    lb a0, 0(t0)      # Load the first character of the string
    li a1, 10         # Load the ASCII value for newline (10)
    beq a0, a1, remove_newline # If newline, proceed to remove it

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

    # Write the string back to STDOUT
    la a0, string_read
    li a7, 4          # Print "String read is: !" message
    ecall

    li a7, 64         # Write syscall
    li a0, 1          # File descriptor (STDOUT)
    la a1, mybuffer   # Buffer address
    mv a2, s0         # Number of characters read
    ecall

    la a0, exclamation
    li a7, 4          # Print exclamation mark
    ecall

    la a0, newline
    li a7, 4          # Print newline
    ecall

    # Print the integer value
    la a0, int_read
    li a7, 4          # Print "Int value read is: !" message
    ecall

    la t0, int1
    lw a0, 0(t0)      # Load integer value
    li a7, 1          # Print integer syscall
    ecall

    la a0, exclamation
    li a7, 4          # Print exclamation mark
    ecall

    la a0, newline
    li a7, 4          # Print newline
    ecall

    # Print the character value
    la a0, char_read
    li a7, 4          # Print "Char value read is: !" message
    ecall

    la t0, mychar
    lb a0, 0(t0)      # Load character value
    li a7, 1          # Print integer (ASCII value) syscall
    ecall

    la a0, exclamation
    li a7, 4          # Print exclamation mark
    ecall

    la a0, newline
    li a7, 4          # Print newline
    ecall

    j read_again      # Loop to read again

remove_newline:
    # Remove newline from buffer by replacing it with null byte
    sb x0, 0(t0)      # Replace the newline character with null byte (end of string)

    # Now print the modified string
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

    # Write the string back to STDOUT
    la a0, string_read
    li a7, 4          # Print "String read is: !" message
    ecall

    li a7, 64         # Write syscall
    li a0, 1          # File descriptor (STDOUT)
    la a1, mybuffer   # Buffer address
    mv a2, s0         # Number of characters read
    ecall

    la a0, exclamation
    li a7, 4          # Print exclamation mark
    ecall

    la a0, newline
    li a7, 4          # Print newline
    ecall

eof_reached:
    # Exit program
    li a7, 10         # Exit syscall
    ecall

