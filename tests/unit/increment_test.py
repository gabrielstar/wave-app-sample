import sys

import pytest

from app.main import increment


# test increment() method
@pytest.mark.parametrize(
    # test parameter names
    "before_increment, after_increment",
    [  # test parameter values, each line defines one individual case:
        (0, 1),  # test_increment_from_zero_to_one
        (sys.maxsize, sys.maxsize + 1),  # test_increment_sys_maxsize
        (1, 2),  # or any other input data we want to test
    ],
)
def test_increment(before_increment, after_increment):
    # Given number is before_increment
    # When incremented, Then it is after_increment
    assert increment(before_increment) == after_increment
