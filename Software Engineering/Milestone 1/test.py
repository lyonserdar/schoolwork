import pytest
from main.py import main, accumulator


def test_read_and_load():
    input_values = [1010, 2010, 4300, 9999, -42]
    output = []

    main.input = ""

    assert accumulator == -42

