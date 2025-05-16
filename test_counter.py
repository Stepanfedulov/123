import pytest
from counter import count_to_ten

def test_count_to_ten():
    result = count_to_ten()
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert len(result) == 10
    assert result[0] == 1
    assert result[-1] == 10