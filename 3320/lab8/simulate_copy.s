# macro_example.s
#
#  java -jar rars1_6.jar macro_example.s
#
# The macro "print_str_label" is from 
#   https://www.robertwinkler.com/projects/riscv_book/riscv_book.html#_macros
# This is renamed here to "print_string".
#
# I added to this.
# -MCW, 2025

.macro print_string(%x)
    li     a7, 4
    la     a0, %x
    ecall
.end_macro

.macro print_char(%x)
    li    a7, 11     
    la    a1, %x
    lb    a0, 0(a1)
    ecall
.end_macro

.text
main:
        # Print the title
        print_string(types_of_apples)

        # Print each type of apple with a preceding space
        print_char(space)
        print_string(apple1)
        print_char(space)
        print_string(apple2)
        print_char(space)
        print_string(apple3)

        # Exit the program with a return code
        li     a7, 93
        li     a0, 42    # 0 for everything is OK, but this uses 42
        ecall

.data 
types_of_apples: .string "Types of apples\n"
apple1:          .string "Fuji\n"
apple2:          .string "Gala\n"
apple3:          .string "Honeycrisp\n"
space:           .byte 0x20
helloworld:      .string "Hello World\n"
char1:           .byte 0x23


