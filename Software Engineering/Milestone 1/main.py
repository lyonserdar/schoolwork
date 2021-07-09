#!/usr/bin/env python

"""
Project: Milestone 1 - UVSim
Group Members:  Ali Aydogdu
                Triston Yocom
                Bryson May
                John Revill
Course: CS 2450-X01
Date Created: 7/3/2021
Date Last Modified: 7/8/2021
"""


class Word:
    """
    Word class is a helper class to provide methods for easy access to sign_bit, opcode,
    operand, and magnitude of an instruction or data that stored in memory
    Author: Ali Aydogdu
    """

    def __init__(self, word="00000"):
        """
        Initialize
        Default word value is "00000"
        """
        self.__word = word

    def get_sign_bit(self):
        """
        Returns the Sign Bit 
        If "1" negative number, otherwise positive number 
        """
        return self.__word[0]

    def get_opcode(self):
        """
        Returns the opcode of the instruction
        """
        return self.__word[1:3]

    def get_operand(self):
        """
        Returns the operand of the instruction
        """
        return self.__word[3:]

    def get_magnitude(self):
        """
        Returns all the bits except sign bit
        This is used when stored data is not an instruction, it is rather pure data
        """
        return self.__word[1:]

    def __str__(self):
        """
        Returns string representation of the word
        """
        return self.__word


class Memory:
    """
    Memory class creates a list of memory locations that can be accessed with index
    The user can specify the memory size, default to 100
    Memory can not grow or shrink
    Author: Ali Aydogdu
    """

    def __init__(self, size=100):
        """
        Initialize
        """
        self.__size = size
        self.__memory = ["00000"] * size

    def clear(self):
        """
        Clears the memory by setting all the locations to "00000"
        """
        for index in range(self.__size):
            self.__memory[index] = "00000"

    def get_size(self):
        """
        Returns the size of the memory
        """
        return self.__size

    def get_data_at(self, location=0):
        """
        Returns the data value at the given memory location
        """
        return self.__memory[location]

    def set_data_at(self, location=0, data="00000"):
        """
        Stores the given data value at the given memory location
        """
        self.__memory[location] = data

    def find_opcode(self, opcode):
        """
        Checks if a specific opcode in the memory
        This is a helper function to see if the code has "HALT"
        Potentially this function does not belong here
        """
        for data in self.__memory:
            if opcode == data[1:3]:
                return True

        return False


class Accumulator:
    """
    Simple function for Accumulator 
    You can set and get the data
    This can be updated to add data validation
    Right now it can store anything
    Author: Ali Aydogdu
    """

    def __init__(self, init_value="00000"):
        """
        Initialize
        """
        self.__data = init_value

    def get_data(self):
        """
        Returns the data stored in accumulator
        """

        return self.__data

    def set_data(self, data):
        """
        Sets the accumulators data
        """

        self.__data = data


class UVSim:
    """
    UVSim 
    Author: Ali Aydogdu
    """

    def __init__(self, memory_size=100, accumulator_init_value="00000"):
        """
        Initialize
        """
        self.__memory = Memory(size=memory_size)
        self.__accumulator = Accumulator(init_value=accumulator_init_value)
        self.__instruction_counter = 0
        self.__current_instruction = Word()
        self.__execution_location = 0

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
                if opcode not in [
                    "00",
                    "10",
                    "11",
                    "20",
                    "21",
                    "30",
                    "31",
                    "32",
                    "33",
                    "40",
                    "41",
                    "42",
                    "43",
                ]:
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
            elif opcode == "10":  # Read
                self.read()
                self.__execution_location += 1
            elif opcode == "11":  # Write
                self.write()
                self.__execution_location += 1
            elif opcode == "20":  # Load
                self.load()
                self.__execution_location += 1
            elif opcode == "21":  # Store
                self.store()
                self.__execution_location += 1
            elif opcode == "30":  # Add
                self.add()
                self.__execution_location += 1
            elif opcode == "31":  # Subtract
                self.subtract()
                self.__execution_location += 1
            elif opcode == "32":  # Divide
                self.divide()
                self.__execution_location += 1
            elif opcode == "33":  # Multiply
                self.multiply()
                self.__execution_location += 1
            elif opcode == "40":  # Branch
                self.__execution_location = self.branch()
            elif opcode == "41":  # BranchNeg
                self.__execution_location = self.branchneg()
            elif opcode == "42":  # BranchZero
                self.__execution_location = self.branchzero()
            elif opcode == "43":  # Halt:
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

    def read(self):
        """
        Reads the word from the keyboard into specific location in memory
        """
        try:
            user_input = input(f"Enter integer value (-9999 to 9999): ")

            value = int(user_input)
            if value > 9999 or value < -9999:
                raise ValueError

            if value < 0:
                data = "1" + f"{abs(value):04d}"
            else:
                data = "0" + f"{value:04d}"
            self.__memory.set_data_at(
                int(self.__current_instruction.get_operand()), data
            )
        except ValueError:
            print("Please enter a valid number between +9999 and -9999!")
            self.read()

    def write(self):
        """
        Writes a word from a specific location in memory to screen 
        """
        data = self.__memory.get_data_at(int(self.__current_instruction.get_operand()))
        print(
            f"Memory address '{self.__current_instruction.get_operand}' contains: {data}"
        )

    def load(self):
        """
        Loads a word from a specific location in memory into the accumulator
        """
        self.__accumulator.set_data(
            self.__memory.get_data_at(int(self.__current_instruction.get_operand()))
        )

    def store(self):
        """
        Stores a word from the accumulator into a specific location in memory
        """
        data = self.__accumulator.get_data()
        self.__memory.set_data_at(int(self.__current_instruction.get_operand()), data)

    def __get_operands(self):
        """
        Helper function that returns the operands to be used in arithmetic calculations
        """
        operand_1 = self.__accumulator.get_data()
        operand_2 = Word(
            self.__memory.get_data_at(int(self.__current_instruction.get_operand()))
        )

        if operand_1[0] == "1":  # Negative Number
            operand_1 = int(operand_1[1:]) * -1
        else:
            operand_1 = int(operand_1[1:])

        if operand_2.get_sign_bit() == "1":  # Negative Number
            operand_2 = int(operand_2.get_magnitude()) * -1
        else:
            operand_2 = int(operand_2.get_magnitude())

        return operand_1, operand_2

    def add(self):
        """
        Adds a word from a specific location in memory to the word in the
        accumulator (leave the result in the accumulator)
        """
        operand_1, operand_2 = self.__get_operands()

        data = "00000"
        value = operand_1 + operand_2

        if value < 0:
            data = "1" + f"{abs(value):04d}"
        else:
            data = "0" + f"{value:04d}"

        self.__accumulator.set_data(data)

    def subtract(self):
        """
        Subtracts a word from a specific location in memory from the word in the
        accumulator (leave the result in the accumulator)
        """
        operand_1, operand_2 = self.__get_operands()

        data = "00000"
        value = operand_1 - operand_2

        if value < 0:
            data = "1" + f"{abs(value):04d}"
        else:
            data = "0" + f"{value:04d}"

        self.__accumulator.set_data(data)

    def divide(self):
        """
        Divides the word in the accumulator by a word from a specific location in
        memory (leave the result in the accumulator)
        """
        operand_1, operand_2 = self.__get_operands()

        data = "00000"
        value = operand_1 / operand_2

        if value < 0:
            data = "1" + f"{abs(value):04d}"
        else:
            data = "0" + f"{value:04d}"

        self.__accumulator.set_data(data)

    def multiply(self):
        """
        Multipies a word from a specific location in memory to the word in the
        accumulator (leave the result in the accumulator)
        """
        operand_1, operand_2 = self.__get_operands()

        data = "00000"
        value = operand_1 * operand_2

        if value < 0:
            data = "1" + f"{abs(value):04d}"
        else:
            data = "0" + f"{value:04d}"

        self.__accumulator.set_data(data)

    def branch(self):
        """
        Branch to a specific location in memory
        """
        value = self.__accumulator.get_data()

        if value[0] == "1":  # Negative Number
            value = int(value[1:]) * -1
        else:
            value = int(value[1:])

        if value > 0:
            return int(self.__current_instruction.get_operand())
        else:
            return self.__execution_location + 1

    def branchneg(self):
        """
        Branch to a specific location in memory if the accumulator is negative
        """
        value = self.__accumulator.get_data()

        if value[0] == "1":  # Negative Number
            value = int(value[1:]) * -1
        else:
            value = int(value[1:])

        if value < 0:
            return int(self.__current_instruction.get_operand())
        else:
            return self.__execution_location + 1

    def branchzero(self):
        """
        Branch to a specific location in memory if the accumulator is zero
        """
        value = self.__accumulator.get_data()

        if value[0] == "1":  # Negative Number
            value = int(value[1:]) * -1
        else:
            value = int(value[1:])

        if value == 0:
            return int(self.__current_instruction.get_operand())
        else:
            return self.__execution_location + 1


def main():
    """
    Main
    Author: Ali Aydogdu
    """
    uvsim = UVSim()
    uvsim.initialize()
    uvsim.program()
    uvsim.execute()
    uvsim.memdump()


if __name__ == "__main__":
    main()
