import pytest
from interview_prep.diningphilosophers import dining_philophers


@pytest.mark.parametrize("test_input,expected", [
        ([1, 2, 3], "firstsecondthird"),
    ])
def test_diningphilosophers(test_input, expected):
    result = dining_philosophers(test_input)
    assert result == expected
