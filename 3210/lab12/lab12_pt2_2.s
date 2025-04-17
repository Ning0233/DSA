# This is written for VSCode/Venus
    # Print 20 random values.
    # -MCW

    .text
    main:
        # Set the seed value
        li    a0, 4             # Set seed to 4
        call  set_seed          # Call set_seed to initialize the seed

        # Initialize the counter
        li    s0, 20            # s0 holds the count
    
    myloop:
        call  get_rand          # Get a random value
        # a0 should now hold a random value    

        # Now print the value out
        mv    a1, a0
        li    a0, 1             # Print an integer
        ecall
    
        # Print space
        li    a0, 11            # Print a character
        li    a1, 32            # Space (the character to print)
        ecall           

        # Update s0 to count down
        addi  s0, s0, -1            
        bgt   s0, x0, myloop    # If greater than 0, jump to myloop
    
        # Print newline
        li    a0, 11            # Print a character
        li    a1, 10            # Newline (the character to print)
        ecall           
        
        # Exit the program
        li    a0, 17
        li    a1, 0             # 0 for everything is OK
        ecall

    # Function to set the seed value
    set_seed:
        la    t0, lfsr          # t0 = address of "lfsr"
        sw    a0, 0(t0)         # Store the value in a0 into "lfsr"
        ret

    # Function to generate a random number
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

    .data       # Data section, initialized variables

    lfsr:      .word  1          # Initial seed value (will be overwritten by set_seed)