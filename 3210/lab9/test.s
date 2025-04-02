.bss
myarray: 10, 4
# define  BUFFER_SIZE  10
#.equ  BUFFER_SIZE  10
.eqv  BUFFER_SIZE  10
# define  BUFFER_SIZE  10
#.equ  BUFFER_SIZE  10
.eqv  BUFFER_SIZE  10

    .eqv  STDIN        0
    .eqv  STDOUT       1
    .eqv  STDERR       2
    .eqv  READ         63
    .eqv  WRITE        64
    .eqv  SIMPLE_READ  8
    .eqv  SIMPLE_WRITE 4
    .eqv  NL           10

    # print str1
    li    a7, SIMPLE_WRITE
    la    a0, str1
    ecall       
