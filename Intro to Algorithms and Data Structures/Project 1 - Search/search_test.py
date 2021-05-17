import pytest
from search import linear_search, binary_search, jump_search
from random import seed, sample
from time import perf_counter
from math import sqrt
import time

DATA_SIZE = 1000000
NOT_IN_LIST = -243687

def make_data():
    seed(0)
    data = sample(range(DATA_SIZE * 3), k=DATA_SIZE)
    data.sort()
    while True:
        yield data

def test_linear_search_at_end_returns_true_when_value_is_in_list():
    gen = make_data()
    data = next(gen)

    result = linear_search(data, data[-1])

    assert result

def test_binary_search_at_end_returns_true_when_value_is_in_list():
    gen = make_data()
    data = next(gen)

    result = binary_search(data, data[-1])

    assert result 

def test_jump_search_at_end_returns_true_when_value_is_in_list():
    gen = make_data()
    data = next(gen)

    result = binary_search(data, data[-1])

    assert result 

def test_linear_search_at_beginning():
    gen = make_data()
    data = next(gen)

    result = linear_search(data, data[0])
    assert result

def test_binary_search_at_beginning():
    gen = make_data()
    data = next(gen)

    result = binary_search(data, data[0])
    assert result


def test_jump_search_at_beginning():
    gen = make_data()
    data = next(gen)

    result = jump_search(data, data[0])
    assert result 

def test_linear_search_at_middle():
    gen = make_data()
    data = next(gen)

    result = linear_search(data, data[(DATA_SIZE // 2) - 1])
    assert result


def test_binary_search_at_middle():
    gen = make_data()
    data = next(gen)

    result = binary_search(data, data[(DATA_SIZE // 2) - 1])
    assert result


def test_jump_search_at_middle():
    gen = make_data()
    data = next(gen)

    result = jump_search(data, data[(DATA_SIZE // 2) - 1])
    assert result

def test_linear_search_not_found():
    gen = make_data()
    data = next(gen)

    result = linear_search(data, NOT_IN_LIST)

    assert not result

def test_binary_search_not_found():
    gen = make_data()
    data = next(gen)

    result = binary_search(data, NOT_IN_LIST)

    assert not result 

def test_jump_search_not_found():
    gen = make_data()
    data = next(gen)

    result = binary_search(data, NOT_IN_LIST)

    assert not result

def test_linear_search_null_list():
    result = linear_search(None, NOT_IN_LIST)

    assert not result

def test_binary_search_null_list():
    result = binary_search(None, NOT_IN_LIST)

    assert not result

def test_jump_search_null_list():
    result = jump_search(None, NOT_IN_LIST)

    assert not result

def test_code_style():
    from pylint import epylint as lint
    import re
    
    (pylint_stdout, pylint_stderr) = lint.py_run('search.py', return_std=True)
    expected = 8.5
    actual = pylint_stdout.getvalue()
    x = re.findall('[0-9]+', actual)[0]
    x = float(x)
    assert x >= expected
