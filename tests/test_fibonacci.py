import pytest
from programs import fibonacci

def test_fibonacci():
    assert fibonacci.fib(0) == 0
    assert fibonacci.fib(1) == 1
    assert fibonacci.fib(2) == 1
    assert fibonacci.fib(5) == 5
    assert fibonacci.fib(1.0) == 1
    assert fibonacci.fib('5') == 5
    assert fibonacci.fib(-3) == "Negative inputs not accepted!"
    assert fibonacci.fib(True) == 1
