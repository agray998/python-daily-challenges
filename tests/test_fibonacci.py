import pytest
from programs import fibonacci

def test_fibonacci_int():
    assert fibonacci.fib(0) == 0
    assert fibonacci.fib(1) == 1
    assert fibonacci.fib(2) == 1
    assert fibonacci.fib(5) == 5

def test_fibonacci_float():
    assert fibonacci.fib(1.0) == 1
    assert fibonacci.fib(7.0) == 13

def test_fibonacci_string():
    assert fibonacci.fib('5') == 5
    assert fibonacci.fib('6') == 8

def test_fibonacci_neg():
    assert fibonacci.fib(-3) == "Negative inputs not accepted!"

def test_fibonacci_bool():
    assert fibonacci.fib(True) == 1
    assert fibonacci.fib(False) == 0
