#!/bin/python
import os
import sys
import pexpect
import time

# emu86.py
# Runs emu86 and passes it the arguments to this script one at a time
# Single letter arguments are passed with the next argument if it is longer than 1 character
# passing a "B" "C" or "T" will be turned into ctrl + that letter in lowercase
# passing a "W" and then a number will delay for that many milliseconds

commands = ([])
i = 1
while i < len(sys.argv):
    if (i+1) < len(sys.argv):
        if(not len(sys.argv[i+1]) == 1):
            commands.append(sys.argv[i] + " " + sys.argv[i+1])
            i += 1
        else: commands.append(sys.argv[i] + " " )
    else: commands.append(sys.argv[i] + " " )
    i += 1

# Create the emu86 process
emu = pexpect.spawn('emu86')

# Run all the commands in order
for command in commands:
    if  (command == "B "): emu.sendcontrol('b')
    elif(command == "C "): emu.sendcontrol('c')
    elif(command == "T "): emu.sendcontrol('t')
    elif("W " in command): 
        time.sleep(float(command.split()[1]) / 1000.0)
    else: emu.sendline(command)

# Pass interaction to the user
emu.interact()
