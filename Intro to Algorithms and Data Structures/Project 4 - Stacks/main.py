#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
I declare that the following source code was written solely by me. I understand that
copying any source code, in whole or in part, constitutes cheating, and that I will
receive a zero on this project if I am found in violation of this policy. 
-
TODO: complete the project description
"""

# * Project 4 - A Stack Machine to Evaluate Expressions

__project__ = "Project 4 - A Stack Machine to Evaluate Expressions"
__author__ = "Ali Serdar Aydogdu"
__email__ = "lyonserdar@gmail.com"
__date__ = "6/20/2021"
__divider__ = "------------------------------------------------------------------------"

from stack import Stack

INPUT_FILE = "data.txt"
OUTPUT_FILE = "output.txt"


def in2post(expression):
    """
    in2post
    """
    # TODO: If the expression is not valid, raise SyntaxError. If the parameter expr is
    # not a string, raise a ValueError.
    if not type(expression) is str:
        raise ValueError
    stack = Stack()
    output = ""
    operators = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    try:
        for input_ in expression.replace(" ", "").strip():
            if input_ == "(":
                stack.push(input_)
            elif input_.isdigit():
                output += input_
            elif input_ in operators:
                while (
                    not stack.is_empty()
                    and stack.top() != "("
                    and operators[stack.top()] >= operators[input_]
                ):
                    output += stack.pop()
                stack.push(input_)
            else:
                # Should be right paranthesis, discard it
                output += stack.pop()
                while stack.top() != "(":
                    output += stack.pop()
                stack.pop()  # Should be left paranthesis, discard it

        while not stack.is_empty():
            output += stack.pop()
    except:
        raise SyntaxError

    return " ".join(output)


def eval_postfix(expression):
    """
    eval_postfix
    """
    # TODO: If the expression is not valid, raise SyntaxError. If the parameter expr is
    # not a string, raise a ValueError.
    if not type(expression) is str:
        raise ValueError
    if not all([len(item) < 2 for item in expression.split(" ")]):
        raise SyntaxError
    stack = Stack()
    for input_ in expression.replace(" ", ""):
        if input_.isdigit():
            stack.push(int(input_))
        else:
            operator = input_
            operand1 = stack.pop()
            operand2 = stack.pop()
            if operator == "*":
                stack.push(operand1 * operand2)
            if operator == "/":
                stack.push(operand2 / operand1)
            if operator == "+":
                stack.push(operand1 + operand2)
            if operator == "-":
                stack.push(operand2 - operand1)

    return stack.pop()


def main():
    """This is the main function"""
    print(__divider__)
    print(__project__)
    print(__divider__)

    with open(INPUT_FILE, "r") as input_file:
        with open(OUTPUT_FILE, "w") as output_file:
            expressions = []
            output = []
            expressions = input_file.read().splitlines()
            for expression in expressions:
                output += f"infix: {expression}\n"
                postfix = in2post(expression)
                output += f"postfix: {postfix}\n"
                answer = eval_postfix(postfix)
                output += f"answer: {answer}\n"
                output += "\n"

            output_file.writelines(output)


if __name__ == "__main__":
    main()
