.text
main:
    # Reserve 100 bytes
    li    a0, 9            # sbrk
    li    a1, 100
    ecall
    la    t0, copy 
    sw    a0, 0(t0)        # Store the address into "copy"

    # Set up pointers
    la    s2, mystring      # s2 points to "mystring"
    la    s3, copy          # s3 points to "copy"
    la    s4, mystring_end  # s4 points to memory after string

    # Copy the string
loop:
    lb    s0, 0(s2)        # Access byte from string
    sb    s0, 0(s3)        # Copy byte to "copy"
    addi  s2, s2, 1        # Increment s2
    addi  s3, s3, 1        # Increment s3
    bne   s2, s4, loop     # Continue until end of string

    # Find the length of the string
    la    a0, mystring     # a0 points to "mystring"
    call  find_len         # Call the subroutine
    mv    t1, a1           # Save the length in t1

    # Print the string with double quotes
    li    a0, 11           # Print a character
    li    a1, 34           # ASCII for double quote (")
    ecall

    li    a0, 4            # Print a string
    la    a1, mystring     # Load address of "mystring"
    ecall

    li    a0, 11           # Print a character
    li    a1, 34           # ASCII for double quote (")
    ecall

    # Print a space
    li    a0, 11
    li    a1, 32           # ASCII for space
    ecall

    # Print the length
    mv    a1, t1           # Move length to a1 (argument for print integer)
    li    a0, 1            # Syscall for print integer
    ecall

    # Print a newline
    li    a0, 11
    li    a1, 10           # ASCII for newline
    ecall

    # Exit the program
    li    a0, 17
    li    a1, 0
    ecall

# Subroutine to find the length of a string
find_len:
    mv    a1, x0           # Set count (a1) to zero
find_len_loop:
    lb    t0, 0(a0)        # Access byte from string
    addi  a0, a0, 1        # Increment a0 (pointer to next byte)
    addi  a1, a1, 1        # Increment a1 (count)
    bne   t0, x0, find_len_loop # Check if byte is not zero
    ret

.data
mystring:  .string "RISC-V Assembly Programming"
mystring_end:
copy:      .word 0