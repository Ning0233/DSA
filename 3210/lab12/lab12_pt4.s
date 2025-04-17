# This is written for VSCode/Venus
    # Generate and print a random string of characters.
    # -MCW

    .text
    main:
        # Define N (number of random characters)
        li   t0, 100            # N = 100
        li   t1, 101            # N+1 for null terminator

        # Reserve space for N+1 bytes
        li   a0, 9              # sbrk syscall
        mv   a1, t1             # a1 = N+1
        ecall
        mv   s1, a0             # s1 = pointer to reserved memory
        mv   s2, s1             # Save the original pointer in s2

        # Populate the first N bytes with random characters
        li   s0, 100            # s0 = loop counter (N)
    populate_loop:
        call get_rand           # Get a random value
        andi t2, a0, 0xF        # Limit to 0-15
        ori  t2, t2, 0x40       # Map to ASCII range 64-79
        sb   t2, 0(s1)          # Store character in memory
        addi s1, s1, 1          # Increment memory pointer
        addi s0, s0, -1         # Decrement counter
        bgt  s0, x0, populate_loop # Repeat until counter is 0

        # Add null terminator at the end
        li   t2, 0              # Null terminator
        sb   t2, 0(s1)          # Store null terminator

        # Print the string
        mv   a0, s2             # Use the saved pointer (s2) to start of string
        li   a1, 100            # Length of string
        call print_string       # Print the string

        # Print newline character
        li   a0, 11             # Print character syscall
        li   a1, 10             # Newline character
        ecall

        # Exit the program
        li   a0, 17             # Exit syscall
        li   a1, 0              # Exit code 0
        ecall

    get_rand:
        la    t2, lfsr          # t2 = address of "lfsr"
        lw    t3, 0(t2)         # t3 = word at "lfsr"

        # Shift t3 left by 11 bits and XOR with itself
        slli  t4, t3, 11        # t4 = t3 << 11
        xor   t3, t3, t4        # t3 = t3 ^ t4

        # Shift t3 right by 7 bits and XOR with itself
        srli  t4, t3, 7         # t4 = t3 >> 7
        xor   t3, t3, t4        # t3 = t3 ^ t4

        # Shift t3 left by 12 bits and XOR with itself
        slli  t4, t3, 12        # t4 = t3 << 12
        xor   t3, t3, t4        # t3 = t3 ^ t4

        # Store the updated value back into "lfsr"
        sw    t3, 0(t2)         # lfsr = t3

        mv    a0, t3            # a0 = t3 to return
        ret

    print_string:
        mv   t0, a0             # t0 = pointer to string
        mv   t1, a1             # t1 = length of string
    print_loop:
        lb   t2, 0(t0)          # Load byte from string
        li   a0, 11             # Print character syscall
        mv   a1, t2             # Character to print
        ecall
        addi t0, t0, 1          # Increment pointer
        addi t1, t1, -1         # Decrement length
        bgt  t1, x0, print_loop # Repeat until length is 0
        ret

    .data       # Data section, initialized variables

    lfsr:      .word  1
