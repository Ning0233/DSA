.text
main:
    # Load the character to look for in t0
    li    t0, ' '          # ASCII for space (' ')
    # Load the address of the string into t1
    la    t1, mystring     # t1 points to "mystring"
    mv    t2, x0           # Initialize space count (t2) to 0

count_spaces:
    lb    t3, 0(t1)        # Load the current character from the string
    beq   t3, x0, write_count # If null terminator (0), exit loop
    bne   t3, t0, skip_inc # If not a space, skip increment
    addi  t2, t2, 1        # Increment space count

skip_inc:
    addi  t1, t1, 1        # Move to the next character
    j     count_spaces     # Repeat the loop

write_count:
    # Print the count of spaces
    mv    a1, t2           # Move space count to a1 (argument for print integer)
    li    a0, 1            # Syscall for print integer
    ecall

    # Print a newline
    li    a0, 11
    li    a1, 10           # ASCII for newline
    ecall

    # Exit the program
    li    a0, 17
    li    a1, 0            # 0 for everything is OK
    ecall

.data
mystring:  .string "RISC-V Assembly Programming"