import pytest
from programs import alphasort

def test_alpha_sort():
    assert alphasort.alpha_sort("hello world and practice makes perfect and hello world again") == "again and hello makes perfect practice world"
    assert alphasort.alpha_sort("1 apple 2 beers") == "1 2 apple beers"
