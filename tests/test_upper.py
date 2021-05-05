import pytest
from programs import upper

def test_upper():
    assert upper.upper_letters("Hello world!") == [('H',0)]
    assert upper.upper_letters("HeLlO wOrLd!") == [('H',0),('L',2),('O',4),('O',7),('L',9)]
