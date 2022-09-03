import pytest
from arithmetic import add, subtract, multiply, divide, int_to_string
from time import perf_counter
import random
import time

def test_add():
    x = random.randint(0,10)
    y = random.randint(0,10)
    expected = x + y
    summ = add(x,y)
    assert summ == expected

def test_subtract():
    x = random.randint(0,10)
    y = random.randint(0,10)
    expected = x - y
    difference = subtract(y,x)
    assert difference == expected

def test_multiply():
    x = random.randint(0,10)
    y = random.randint(0,10)
    expected = x * y
    product = multiply(x,y)
    assert product == expected

def test_divide():
    x = random.randint(1,10)
    y = random.randint(1,10)
    expected = x / y
    quotient = divide(y,x)
    assert quotient == expected

def test_int_to_string():
    x = random.randint(0,10)
    s = int_to_string(x)
    assert s == str(x)

def test_code_style():
    from pylint.lint import Run
    
    results = Run(['arithmetic.py'], exit=False)
    expected = 8.5
    actual = results.linter.stats['global_note']
    assert actual >= expected
