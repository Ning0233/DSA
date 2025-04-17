# This is written for VSCode/Venus
    # Print 20 random values.
    # -MCW

    .text
    main:
        # Note: we use s0 to make sure the value does not change 
        # when we do a call/ecall 
        li   s0, 20              # s0 holds the count
    
    myloop:
        call   get_rand          # get a random value
    
        # Now print the value out
        mv     a1, a0
        li     a0, 1      # print an integer
        ecall
    
        # print space
        li    a0, 11     # print a character
        li    a1, 32     # space (the character to print)
        ecall           

        # Update s0 to count down
        addi   s0, s0, -1            
        bgt    s0, x0, myloop       # if greater or equal, jump to myloop
    
        # print NL
        li    a0, 11     # print a character
        li    a1, 10     # NL (the character to print)
        ecall           
        
        # exit the program
        li     a0, 17
        li     a1, 0                # 0 for everything is OK
        ecall

    get_rand:
        la    t2, lfsr        # t2 = address of "lfsr"
        lw    t3, 0(t2)       # t3 = word at "lfsr"

        # Shift t3 left by 11 bits and XOR with itself
        slli  t4, t3, 11      # t4 = t3 << 11
        xor   t3, t3, t4      # t3 = t3 ^ t4

        # Shift t3 right by 7 bits and XOR with itself
        srli  t4, t3, 7       # t4 = t3 >> 7
        xor   t3, t3, t4      # t3 = t3 ^ t4

        # Shift t3 left by 12 bits and XOR with itself
        slli  t4, t3, 12      # t4 = t3 << 12
        xor   t3, t3, t4      # t3 = t3 ^ t4

        # Store the updated value back into "lfsr"
        sw    t3, 0(t2)       # lfsr = t3

        mv    a0, t3          # a0 = t3 to return
        ret


    .data       # Data section, initialized variables

    lfsr:      .word  1
