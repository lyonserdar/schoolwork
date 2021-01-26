__class__ = "CS 1410"
__project__ = "Programming Exercise 4.9"
__author__ = "Ali Serdar Aydogdu"
__email__ = "lyonserdar@gmail.com"
__date__ = "1/15/2021"
__divider__ = "------------------------------------------------------------------------"

"""
Prompt the user for the names of two files. The input filename could be the name of the
script itself, but be careful to use a different output filename! The script copies the
lines of text from the input file to the output file, numbering each line as it goes.
The line numbers should be right-justified in 4 columns, so that the format of a line in
the output file looks like this example:
   1> This is the first line of text.
"""

input_file = input("Input: ")
output_file = input("Output: ")

lines = []

with open(input_file, "r") as f:
    lines = f.readlines()

for index, line in enumerate(lines):
    lines[index] = f"{str(index + 1).rjust(4)}> {line}"

with open(output_file, "w") as f:
    f.writelines(lines)
        