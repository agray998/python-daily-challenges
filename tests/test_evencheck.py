import pytest
import evencheck


def test_check_even():
    assert evencheck.check_even(0) == True
    assert evencheck.check_even(2) == True
    assert evencheck.check_even(3) == False
    assert evencheck.check_even(5) == False
