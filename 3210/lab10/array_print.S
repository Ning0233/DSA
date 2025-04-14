.data       # Data section, initialized variables

myarr:     .word 10, 20, 30, 40, 50, 60
myarr_end: # This will be next word after myarr
temp:      .word 0
# This is written for VSCode/Venus

.text
main:
    # Note: we use s0 to make sure the value does not change 
    # when we do a call/ecall 
    la   s0, myarr              # s0 points to myarr

myloop:
    lw   t1,  0(s0)              # Get the value  t1 = myarr[s0]    

    # Now print the array value out
    mv     a1, t1
    li     a0, 1      # print an integer
    ecall

    # print space
    li    a0, 11     # print a character
    li    a1, 32     # space (the character to print)
    ecall           

    # Update s0 to point to next word
    addi   s0, s0, 4            
    la     t1, myarr_end        # Does s0 == address of word beyond myarr?
    blt    s0, t1, myloop       # if less, jump to myloop

    # print NL
    li    a0, 11     # print a character
    li    a1, 10     # NL (the character to print)
    ecall           
    
    # exit the program
    li     a0, 17
    li     a1, 0                # 0 for everything is OK
    ecall