import pytest
from programs import evencheck


def test_is_prime():
    assert evencheck.is_prime(2) == True
    assert evencheck.is_prime(3) == True
    assert evencheck.is_prime(4) == False
    assert evencheck.is_prime(6) == False



def test_check_even():
    assert evencheck.check_even(0) == True
    assert evencheck.check_even(2) == True
    assert evencheck.check_even(3) == False
    assert evencheck.check_even(5) == False
