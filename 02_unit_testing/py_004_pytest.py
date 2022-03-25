import pytest
from py_002_ut_odd_even import py_002_ut_odd_even


def test_num():
    assert sum([1, 2, 3]) == 6


def test_sum_tuple():
    assert sum((5, 15, 5)) == 30


def test_odd():
    assert py_002_ut_odd_even([1, 2, 3, 4], 1) == [1, 3]


def test_even():
    assert py_002_ut_odd_even([1, 2, 3, 4, 5], 0) == [2, 4, 6]


def test_odd_empty():
    assert py_002_ut_odd_even([2, 4, 6], 1) == [2]


def test_even_empty():
    assert py_002_ut_odd_even([1, 3, 5], 0) == [1]
