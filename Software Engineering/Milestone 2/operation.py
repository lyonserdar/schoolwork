"""
Operation Class
Author: Ali Aydogdu
Course: CS 2450-X01
Date Created: 7/9/2021
Date Last Modified: 7/9/2021
"""

from abc import ABC, abstractmethod
from word import Word


class Operation(ABC):
    """
    Abstract class for Operation
    """

    def __init__(self, opcode):
        self.__opcode = opcode

    @abstractmethod
    def compute(self, memory, accumulator, operand):
        """
        Does what operations is suppose to do
        """
        pass


class ArithmeticOperation(Operation):
    """
    Abstract class for Arithmetic Operation
    """

    def __init__(self, opcode):
        Operation.__init__(self, opcode)

    @abstractmethod
    def compute(self, memory, accumulator, operand):
        pass

    def get_operands(self, memory, accumulator, operand):
        """
        Helper function that returns the operands to be used in arithmetic calculations
        """
        operand_1 = Word(accumulator.get_data())
        operand_2 = Word(memory.get_data_at(int(operand)))

        if operand_1.get_sign_bit() == "1":  # Negative Number
            operand_1 = int(operand_1.get_magnitude()) * -1
        else:
            operand_1 = int(operand_1.get_magnitude())

        if operand_2.get_sign_bit() == "1":  # Negative Number
            operand_2 = int(operand_2.get_magnitude()) * -1
        else:
            operand_2 = int(operand_2.get_magnitude())

        return operand_1, operand_2


class Read(Operation):
    """
    Reads the word from the keyboard into specific location in memory
    """

    def __init__(self, opcode):
        super().__init__(opcode)

    def compute(self, memory, accumulator, operand):
        """
        TODO
        """
        memory.set_data_at(int(operand), self.get_user_input())

    def get_user_input(self):
        """
        TODO
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

            return data
        except ValueError:
            print("Please enter a valid number between +9999 and -9999!")
            self.get_user_input()


class Write(Operation):
    """
    Writes a word from a specific location in memory to screen 
    """

    def __init__(self, opcode):
        super().__init__(opcode)

    def compute(self, memory, accumulator, operand):
        """
        TODO
        """
        data = memory.get_data_at(int(operand))
        print(f"Memory address '{int(operand)}' contains: {data}")


class Load(Operation):
    """
    Loads a word from a specific location in memory into the accumulator
    """

    def __init__(self, opcode):
        super().__init__(opcode)

    def compute(self, memory, accumulator, operand):
        """
        TODO
        """
        accumulator.set_data(memory.get_data_at(int(operand)))


class Store(Operation):
    """
    Stores a word from the accumulator into a specific location in memory
    """

    def __init__(self, opcode):
        super().__init__(opcode)

    def compute(self, memory, accumulator, operand):
        """
        TODO
        """
        memory.set_data_at(int(operand), accumulator.get_data())


class Add(ArithmeticOperation):
    """
    Adds a word from a specific location in memory to the word in the
    accumulator (leave the result in the accumulator)
    """

    def __init__(self, opcode):
        super().__init__(opcode)

    def compute(self, memory, accumulator, operand):
        """
        TODO
        """
        operand_1, operand_2 = self.get_operands(memory, accumulator, operand)
        data = "00000"
        value = operand_1 + operand_2

        if value < 0:
            data = "1" + f"{abs(value):04d}"
        else:
            data = "0" + f"{value:04d}"

        accumulator.set_data(data)


class Subtract(ArithmeticOperation):
    """
    Subtracts a word from a specific location in memory from the word in the
    accumulator (leave the result in the accumulator)
    """

    def __init__(self, opcode):
        super().__init__(opcode)

    def compute(self, memory, accumulator, operand):
        """
        TODO
        """
        operand_1, operand_2 = self.get_operands(memory, accumulator, operand)

        data = "00000"
        value = operand_1 - operand_2

        if value < 0:
            data = "1" + f"{abs(value):04d}"
        else:
            data = "0" + f"{value:04d}"

        accumulator.set_data(data)


class Divide(ArithmeticOperation):
    """
    Divides the word in the accumulator by a word from a specific location in
    memory (leave the result in the accumulator)
    """

    def __init__(self, opcode):
        super().__init__(opcode)

    def compute(self, memory, accumulator, operand):
        """
        TODO
        """
        operand_1, operand_2 = self.get_operands(memory, accumulator, operand)

        data = "00000"
        value = operand_1 / operand_2

        if value < 0:
            data = "1" + f"{abs(value):04d}"
        else:
            data = "0" + f"{value:04d}"

        accumulator.set_data(data)


class Multiply(ArithmeticOperation):
    """
    Multipies a word from a specific location in memory to the word in the
    accumulator (leave the result in the accumulator)
    """

    def __init__(self, opcode):
        super().__init__(opcode)

    def compute(self, memory, accumulator, operand):
        """
        TODO
        """
        operand_1, operand_2 = self.get_operands(memory, accumulator, operand)

        data = "00000"
        value = operand_1 * operand_2

        if value < 0:
            data = "1" + f"{abs(value):04d}"
        else:
            data = "0" + f"{value:04d}"

        accumulator.set_data(data)


class Branch(Operation):
    """
    Branch to a specific location in memory
    """

    def __init__(self, opcode):
        super().__init__(opcode)

    def compute(self, memory, accumulator, operand):
        """
        TODO
        """
        value = Word(accumulator.get_data())

        if value.get_sign_bit() == "1":  # Negative Number
            value = int(value.get_magnitude()) * -1
        else:
            value = int(value.get_magnitude())

        if value > 0:
            return int(operand)


class BranchNeg(Operation):
    """
    Branch to a specific location in memory if the accumulator is negative
    """

    def __init__(self, opcode):
        super().__init__(opcode)

    def compute(self, memory, accumulator, operand):
        """
        TODO
        """
        value = Word(accumulator.get_data())

        if value.get_sign_bit() == "1":  # Negative Number
            value = int(value.get_magnitude()) * -1
        else:
            value = int(value.get_magnitude())

        if value < 0:
            return int(operand)


class BranchZero(Operation):
    """
    Branch to a specific location in memory if the accumulator is zero
    """

    def __init__(self, opcode):
        super().__init__(opcode)

    def compute(self, memory, accumulator, operand):
        """
        TODO
        """
        value = Word(accumulator.get_data())

        if value.get_sign_bit() == "1":  # Negative Number
            value = int(value.get_magnitude()) * -1
        else:
            value = int(value.get_magnitude())

        if value == 0:
            return int(operand)


class Halt(Operation):
    """
    Pause the program
    """

    def __init__(self, opcode):
        super().__init__(opcode)

    def compute(self, memory, accumulator, operand):
        """
        TODO
        """
        pass
