#!/usr/bin/env python
"""
UVSim Class
Author: Ali Aydogdu
Course: CS 2450-X01
Date Created: 7/9/2021
Date Last Modified: 7/9/2021
"""

from word import Word
from memory import Memory
from accumulator import Accumulator
from operation import (
    Read,
    Write,
    Load,
    Store,
    Add,
    Subtract,
    Divide,
    Multiply,
    Branch,
    BranchNeg,
    BranchZero,
    Halt,
)


class UVSim:
    """
    UVSim
    """

    def __init__(self, memory_size=100, accumulator_init_value="00000"):
        self.__memory = Memory(size=memory_size)
        self.__accumulator = Accumulator(init_value=accumulator_init_value)
        self.__instruction_counter = 0
        self.__current_instruction = Word()
        self.__execution_location = 0
        self.__setup()

    def __setup(self):
        """
        TODO
        """
        read = Read("10")
        write = Write("11")
        load = Load("20")
        store = Store("21")
        add = Add("30")
        subtract = Subtract("31")
        divide = Divide("32")
        multiply = Multiply("33")
        branch = Branch("40")
        branchneg = BranchNeg("41")
        branchzero = BranchZero("42")
        halt = Halt("43")

        self.__operations = {
            "10": read,
            "11": write,
            "20": load,
            "21": store,
            "30": add,
            "31": subtract,
            "32": divide,
            "33": multiply,
            "40": branch,
            "41": branchneg,
            "42": branchzero,
            "43": halt,
        }

    def initialize(self):
        """
        Initializes the program by reseting memory and other components
        Displays user instructions
        """
        self.__memory.clear()
        print("UVSim")
        print("Enter instructions:")
        print("To exit and run the program type 9999")

    def program(self):
        """
        Starts the program from location 00  
        Prompts user for instructions
        """
        program_memory_location = 0

        while program_memory_location < self.__memory.get_size():
            try:
                user_input = input(f"{program_memory_location:02d} > ")
                if len(user_input) != 4:
                    raise ValueError
                if not user_input.isnumeric():
                    raise ValueError
                instruction = "0" + user_input
                opcode = instruction[1:3]
                operand = instruction[3:]
                if opcode == "99":  # End Program
                    break
                if opcode not in self.__operations and instruction != "00000":
                    raise ValueError
                self.__memory.set_data_at(program_memory_location, instruction)
                program_memory_location += 1
            except ValueError:
                print("Please enter a valid instruction")
                print("or type 9999 to end programming!")

    def execute(self):
        """
        Executes the program
        """
        opcode = 0

        if not self.__memory.find_opcode("43"):
            print(f"Please include HALT(4300) command in code!")
            return

        print("-*-Execution Started-*-")

        while opcode != "43":
            self.__instruction_counter += 1
            self.__current_instruction = Word(
                self.__memory.get_data_at(self.__execution_location)
            )
            opcode = self.__current_instruction.get_opcode()
            operand = self.__current_instruction.get_operand()

            if opcode == "00":  # Skip
                self.__execution_location += 1
                continue

            address = self.__operations[opcode].compute(
                self.__memory, self.__accumulator, operand
            )

            if address:
                self.__execution_location = address
            else:
                self.__execution_location += 1

            if opcode == "43":  # Halt
                break

        print("-*-Execution Ended-*-")
        print("-*-Statistics-*-")
        print(f"Accumulator: {self.__accumulator.get_data()}")
        print(f"Instruction Count: {self.__instruction_counter}")
        print(f"Last Instruction: {self.__current_instruction}")

    def memdump(self):
        """
        Prints the memory image on the screen
        """
        print("-*-Memory-*-")
        print(" " * 2, end="")
        for i in range(10):
            print(" " * 5 + str(i), end="")
        print()
        for index in range(self.__memory.get_size()):
            if index % 10 == 0:
                if index > 0:
                    print(f"\n{index // 10}0", end=" ")
                else:
                    print(f"{index // 10}0", end=" ")
            print(self.__memory.get_data_at(location=index), end=" ")
        print()

