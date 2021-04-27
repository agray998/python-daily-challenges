import pytest
from programs import evendigits

def test_is_prime():
    assert evendigits.is_prime(2) == True
    assert evendigits.is_prime(3) == True
    assert evendigits.is_prime(4) == False
    assert evendigits.is_prime(6) == False



def test_check_even():
    assert evendigits.check_even(0) == True
    assert evendigits.check_even(2) == True
    assert evendigits.check_even(3) == False
    assert evendigits.check_even(5) == False


def test_evendigits():
    assert evendigits.even_digits(10, 30) == "20,22,24,26,28,"
    assert evendigits.even_digits(10, 50) == "20,22,24,26,28,40,42,44,46,48,"
