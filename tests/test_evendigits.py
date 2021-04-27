import pytest
from programs import evendigits

def test_evendigits():
    assert evendigits.even_digits(10, 30) == "20,22,24,26,28,"
    assert evendigits.even_digits(10, 50) == "20,22,24,26,28,40,42,44,46,48,"
