import pytest
from interview_prep.diagonaldifference import diagonal_difference


@pytest.mark.parametrize("test_input,expected", [
    ([[]], 0),
    ([[1, 1], [5, 2]], 3),
    ([[11, 2, 4], [4, 5, 6], [10, 8, -12]], 15),
    ])
def test_diagonal_difference(test_input, expected):
    result = diagonal_difference(test_input)
    assert result == expected
