# This is an assembly language program written for the Venus simulator
#

.text

main:
   lw    t0, int2
                          # Now print the result out
   mv    a1, t0           # Value to print
   li    a0, 1            # ecall ID for printing an integer
   ecall 

   li    a0, 11     
   li    a1, 10
   ecall                  # adds a newline

   li    a0, 10           # ecall ID for exiting the program
   ecall

   ret

.data

    # Define integer values
int1: .word 10
int2: .word 5
sum:  .double 0

