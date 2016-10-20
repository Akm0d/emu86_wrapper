# emu86_wrapper
BYU ECEN 425 emu86 command line tool

Runs emu86 and passes it the arguments to this script one at a time
Single letter arguments are passed with the next argument if it is longer than 1 character
passing a "B" "C" or "T" will be turned into ctrl + that letter in lowercase
passing a "W" and then a number will delay for that many milliseconds

# EXAMPLES:
$ ./emu86.py l yak.bin t 750 e B q

OUTPUT:
Welcome to the BYU ECEn 425 8086 simulator.
For a list of commands, enter h or ?.

Emu86>l yak.bin
File "yak.bin" loaded at address 0000:0000 (CS:IP -> 0000:0100).
Emu86>t 750
Tick inverval set to 750.
Emu86>e
< Manual break > - Program not yet terminated.
Emu86>q

$ ./emu86.py h q

OUTPUT:
Welcome to the BYU ECEn 425 8086 simulator.
For a list of commands, enter h or ?.

Emu86>v
Verbose mode now ON
Emu86>h
Paramater Formats:
 Addresses:   Addresses can be of the following forms:
                1) SEG:OFF          (Hex segment and offset)
                2) ABh, 0xAB        (Hex)
                3) 171              (Decimal)
                4) Label            (A symbolic label from the listing file)
 Numbers:     Numbers can be hex (e.g. ABh, 0xAB) or decimal (e.g. 171)

Command Descriptions:
 Ctrl+B        Press Ctrl+B to force a manual break in program execution.
 a N           Assert IRQ number N.
 addr SYMBOL   Give the address associated with the label SYMBOL.
 b             Display current breakpoints and information.
 b ADDR        Set breakpoint for instruction located at ADDR.
 c ID          Clear breakpoint with given ID, use ID 'all' to clear all.
 clear         Clear all breakpoints, memory watches, and register watches.
 d [ADDR]
Emu86>q
