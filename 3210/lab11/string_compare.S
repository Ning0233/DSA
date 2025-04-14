.text
main:
    # Print the first string
    la    a1, mystring1        # Load address of mystring1
    li    a0, 4                # Syscall for print string
    ecall

    # Print a newline
    li    a0, 11
    li    a1, 10               # ASCII for newline
    ecall

    # Print the second string
    la    a1, mystring2        # Load address of mystring2
    li    a0, 4                # Syscall for print string
    ecall

    # Print a newline
    li    a0, 11
    li    a1, 10               # ASCII for newline
    ecall

    # Load the addresses of the two strings into t0 and t1
    la    t0, mystring1        # t0 points to "RISC-v Assembly Programming"
    la    t1, mystring2        # t1 points to "RISC-V Assembly Programming"

    # Call the compare_strings subroutine
    call  compare_strings

    # Check the result in t2
    beq   t2, x0, print_equal  # If t2 == 0, strings are equal
    j     print_not_equal      # Otherwise, strings are not equal

print_equal:
    # Print "equal"
    la    a1, equal_msg        # Load address of "equal"
    li    a0, 4                # Syscall for print string
    ecall
    j     exit_program

print_not_equal:
    # Print "not equal"
    la    a1, not_equal_msg    # Load address of "not equal"
    li    a0, 4                # Syscall for print string
    ecall

exit_program:
    # Exit the program
    li    a0, 17
    li    a1, 0                # 0 for everything is OK
    ecall

# Subroutine to compare two strings
compare_strings:
    mv    t2, x0               # Initialize t2 to 0 (assume strings are equal)

compare_loop:
    lb    t3, 0(t0)            # Load byte from first string
    lb    t4, 0(t1)            # Load byte from second string
    bne   t3, t4, not_equal    # If bytes are not equal, set t2 to 1
    beq   t3, x0, equal        # If null terminator, strings are equal
    addi  t0, t0, 1            # Move to next character in first string
    addi  t1, t1, 1            # Move to next character in second string
    j     compare_loop         # Repeat the loop

not_equal:
    li    t2, 1                # Set t2 to 1 (strings are not equal)
    ret

equal:
    ret

.data
mystring1:      .string "RISC-V Assembly Programming"
mystring2:      .string "RISC-V Assembly Programming"
equal_msg:      .string "equal\n"
not_equal_msg:  .string "not equal\n"