#!/usr/bin/env python

"""
Project: Milestone 1 - UVSim
Authors: Ali Aydogdu
         Triston Yocom
         Bryson May
         John Revill
Course: CS 2450-X01
Date Created: 7/3/2021
Date Last Modified: 7/3/2021
"""

# ? Instructions that don't require operand, ignore or error
# ? Branch specifications, assumed it checks the accumulator
# ? How to represent negative numbers
# ? When loading number want signed word or regular int

memory = [0] * 100
accumulator = 0
instruction_counter = 0
opcodes = {
    0: "SKIP",
    10: "READ",
    11: "WRITE",
    20: "LOAD",
    21: "STORE",
    30: "ADD",
    31: "SUBTRACT",
    32: "DIVIDE",
    33: "MULTIPLY",
    40: "BRANCH",
    41: "BRANCHNEG",
    42: "BRANCHZERO",
    43: "HALT",
    99: "END",
}


def initialize():
    """
    Initializes the program by reseting memory
    Author: Ali Aydogdu
    """
    for index in range(len(memory)):
        memory[index] = 0


def start():
    """
    Starts the program from location 00  
    Prompts user for instructions
    Author: Ali Aydogdu
    """
    location = 0

    while location < len(memory):
        try:
            user_input = input(f"{location:02d} > ")
            if len(user_input) != 4:
                raise ValueError
            insruction = int(user_input)
            opcode = insruction // 100
            operand = insruction % 100
            if opcodes[opcode] == "END":  # End Program
                break
            if opcode not in opcodes:
                raise ValueError
            memory[location] = insruction
            # print(opcodes[opcode], operand)
            location += 1
        except ValueError:
            print("Please enter a valid instruction or type 9999 to end programming!")


def execute():
    """
    Executes the program
    Author: Ali Aydogdu
    """
    global instruction_counter
    opcode = 0
    location = 0
    halt_flag = False

    for address in memory:
        if opcodes[address // 100] == "HALT":
            halt_flag = True
            break

    if not halt_flag:
        print(f"Please include HALT(4300) command in code!")
        return

    while opcodes[opcode] != "HALT":
        instruction_counter += 1
        insruction = memory[location]
        opcode = insruction // 100
        operand = insruction % 100
        if opcode == 43:
            break
        if opcode == 0:
            location += 1
            continue
        address = operations[opcodes[opcode]](operand)
        if address:
            location = address
        else:
            location += 1


def end():
    """
    Displays the end stats
    Author: Ali Aydogdu
    """
    print("-*-Execution Terminated-*-")
    print(f"Accumulator: {accumulator}")
    print(f"Instruction Count: {instruction_counter}")


# Implementation of DEBUG instructions
def memdump():
    """
    Prints the memory image on the screen
    Author: Ali Aydogdu
    """
    print("Memory:")
    print(" " * 2, end="")
    for i in range(10):
        print(" " * 5 + str(i), end="")
    print()
    for index, value in enumerate(memory):
        if index % 10 == 0:
            if index > 0:
                print(f"\n{index // 10}0", end=" ")
            else:
                print(f"{index // 10}0", end=" ")
        if value < 0:
            value = -1 * value + 10000
        print(f"{value:05d}", end=" ")
    print()


def debug_break():
    """
    TODO: Missing
    Author: 
    """


def debug_continue():
    """
    TODO: Missing
    Author: 
    """
    pass


# Implementation of instructions
def read(operand):
    """
    Reads the word from the keyboard into specific location in memory
    Author: Ali Aydogdu
    """
    try:
        user_input = input(f"Enter integer value for memory address '{operand}': ")
        if len(user_input) > 4:
            raise ValueError

        memory[operand] = int(user_input)
    except ValueError:
        print("Please enter a valid number between +9999 and -9999!")


def write(operand):
    """
    ? Outputs the value of specified memory location to console 
    Author: Ali Aydogdu
    """
    print(f"Memory address '{operand}' contains: {memory[operand]}")


def load(operand):
    """
    Loads a word from a specific location in memory into the accumulator
    Author: Ali Aydogdu
    """
    global accumulator
    print(
        f"Memory address '{operand}' that contains {memory[operand]} loaded to accumulator"
    )
    accumulator = memory[operand]


def store(operand):
    """
    ? Stores the accumulator to specified memory
    Author: Ali Aydogdu
    """
    global accumulator
    memory[operand] = accumulator
    print(f"Value {accumulator} stored to memory address '{operand}'")


def add(operand):
    """
    Adds a word from a specific location in memory to the word in the accumulator
    (leave the result in the accumulator)
    Author: Ali Aydogdu
    """
    global accumulator
    accumulator = memory[operand] + accumulator
    print(f"numbers added: {accumulator}")


def subtract(operand):
    """
    TODO: Missing
    Author: Ali Aydogdu
    """
    global accumulator
    print("DEBUG", memory[operand], accumulator, memory[operand] - accumulator)
    accumulator -= memory[operand]
    print(f"numbers subtracted: {accumulator}")


def divide(operand):
    """
    TODO: Missing
    Author: Ali Aydogdu
    """
    global accumulator
    accumulator = memory[operand] / accumulator
    print(f"numbers divided: {accumulator}")


def multiply(operand):
    """
    TODO: Missing
    Author: Ali Aydogdu
    """
    global accumulator
    accumulator = memory[operand] * accumulator
    print(f"numbers multiplied: {accumulator}")


def branch(operand):
    """
    Branch to a specific location in memory
    Author: Ali Aydogdu
    """
    global accumulator
    if accumulator > 0:
        return operand


def branchneg(operand):
    """
    TODO: Missing
    Author: Ali Aydogdu
    """
    global accumulator
    if accumulator < 0:
        return operand


def branchzero(operand):
    """
    TODO: Missing
    Author: Ali Aydogdu
    """
    global accumulator
    if accumulator == 0:
        return operand


# This is located here because functions needed to be declared before this dictionary
operations = {
    "READ": lambda operand: read(operand),
    "WRITE": lambda operand: write(operand),
    "LOAD": lambda operand: load(operand),
    "STORE": lambda operand: store(operand),
    "ADD": lambda operand: add(operand),
    "SUBTRACT": lambda operand: subtract(operand),
    "DIVIDE": lambda operand: divide(operand),
    "MULTIPLY": lambda operand: multiply(operand),
    "BRANCH": lambda operand: branch(operand),
    "BRANCHNEG": lambda operand: branchneg(operand),
    "BRANCHZERO": lambda operand: branchzero(operand),
}


def main():
    """
    Main
    Author: Ali Aydogdu
    """
    print("UVSim")
    print("Enter instructions:")
    print("To exit and run the program type 9999")
    initialize()
    start()
    execute()
    end()
    memdump()


if __name__ == "__main__":
    main()
