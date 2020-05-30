import pytest
from interview_prep.removedupesfromsortedarray import remove_duplicates



@pytest.mark.parametrize("test_input,expected", [
        ([1, 1], [1]),
        ([1, 1, 2], [1, 2]),
        ([0,0,0,0,0], [0]),
        ([1,1,1,1,1], [1]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4]),
    ])
def test_remove_duplicates(test_input, expected):
    result = remove_duplicates(test_input)
    assert result == expected
