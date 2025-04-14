.text
    main:
        # Initialize pointers and variables
        la   s0, myarr              # s0 points to myarr
        lw   t0, 0(s0)              # Load the first value of myarr into t0
        la   t4, min_val            # Load the address of min_val
        sw   t0, 0(t4)              # Initialize min_val with the first value
        la   t4, max_val            # Load the address of max_val
        sw   t0, 0(t4)              # Initialize max_val with the first value
        li   t1, 0                  # Initialize sum to 0
        li   a0, 4                  # Print "The array has the following values:"
        la   a1, array_msg
        ecall

    myloop:
        lw   t2, 0(s0)              # Load the current value of myarr into t2
        add  t1, t1, t2             # Add the current value to the sum

        # Check for minimum value
        la   t4, min_val            # Load the address of min_val
        lw   t3, 0(t4)              # Load the current minimum value
        blt  t2, t3, update_min     # If t2 < t3, update min_val
        j    check_max              # Otherwise, skip to max check
    update_min:
        sw   t2, 0(t4)              # Update min_val with the current value

    check_max:
        la   t4, max_val            # Load the address of max_val
        lw   t3, 0(t4)              # Load the current maximum value
        bgt  t2, t3, update_max     # If t2 > t3, update max_val
        j    print_value            # Otherwise, skip to printing
    update_max:
        sw   t2, 0(t4)              # Update max_val with the current value

    print_value:
        mv   a1, t2                 # Move the current value to a1 for printing
        li   a0, 1                  # Print an integer
        ecall

        # Print space
        li   a0, 11                 # Print a character
        li   a1, 32                 # Space (the character to print)
        ecall

        # Update s0 to point to the next word
        addi s0, s0, 4
        la   t4, myarr_end          # Check if s0 == address of word beyond myarr
        blt  s0, t4, myloop         # If less, jump to myloop

    # Print newline after array values
        li   a0, 11
        li   a1, 10                 # Newline (the character to print)
        ecall

    # Calculate and print average
        li   t5, 6                  # Array length
        div  t6, t1, t5             # Average = sum / array length
        la   a1, avg_msg
        li   a0, 4                  # Print "The average value is:"
        ecall
        mv   a1, t6                 # Move average to a1 for printing
        li   a0, 1                  # Print an integer
        ecall

    # Print minimum value
        la   a1, min_msg
        li   a0, 4                  # Print "The minimum value is:"
        ecall
        la   t4, min_val            # Load the address of min_val
        lw   a1, 0(t4)              # Load min_val for printing
        li   a0, 1                  # Print an integer
        ecall

    # Print maximum value
        la   a1, max_msg
        li   a0, 4                  # Print "The maximum value is:"
        ecall
        la   t4, max_val            # Load the address of max_val
        lw   a1, 0(t4)              # Load max_val for printing
        li   a0, 1                  # Print an integer
        ecall

    # Exit the program
        li   a0, 17
        li   a1, 0                  # 0 for everything is OK
        ecall

.data       # Data section, initialized variables
    myarr:     .word 90, 120, 10
    myarr_end: # This will be next word after myarr
    temp:      .word 0
    min_val:   .word 0
    max_val:   .word 0
    array_msg: .asciiz "The array has the following values:\n"
    avg_msg:   .asciiz "The average value is:\n"
    min_msg:   .asciiz "The minimum value is:\n"
    max_msg:   .asciiz "The maximum value is:\n"