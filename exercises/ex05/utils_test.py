"""Tests the functions in utils file"""

__author__ = "730481454"

from exercises.ex05.utils import only_evens, sub, add_at_index


# tests for only_even function
def test_only_even_return() -> None:
    """tests the only_even function returns what its supposed to"""
    list_1: list[int] = [1, 3, 4, 5, 7, 8, 10]
    assert only_evens(list_1) == [4, 8, 10]


def test_only_even_use() -> None:
    """tests the only_even function does what it is supposed to do"""
    list_1: list[int] = [1, 3, 4, 5, 7, 8, 10]
    only_evens(list_1)
    assert list_1 == [1, 3, 4, 5, 7, 8, 10]


def test_only_even_edge() -> None:
    """tests the only_even function for if the list is empty"""
    list_2: list[int] = []
    assert only_evens(list_2) == []


# tests for sub function
def test_sub_return() -> None:
    """tests the sub function for if it return whats its supposed to return"""
    list_1: list[int] = [1, 3, 4, 5, 7, 8, 10]
    assert sub(list_1, 1, 3) == [3, 4]


def test_sub_use() -> None:
    """tests the sub function for if it does whats its supposed to do"""
    list_1: list[int] = [1, 3, 4, 5, 7, 8, 10]
    sub(list_1, 1, 3)
    assert list_1 == [1, 3, 4, 5, 7, 8, 10]


def test_sub_edge() -> None:
    """tests the sub function if the list is empty"""
    list_2: list[int] = []
    assert sub(list_2, 1, 3) == []


# tests for test_add_at_index function
def test_add_at_index_return() -> None:
    """tests the add_at_index for if it returns the correct thing"""
    list_1: list[int] = [1, 3, 4, 5, 7, 8, 10]
    assert add_at_index(list_1, 1, 3) == None


def test_add_at_index_use() -> None:
    """tests the add_at_index for if it does what it is supposed to do"""
    list_1: list[int] = [1, 3, 4, 5, 7, 8, 10]
    add_at_index(list_1, 1, 3)
    assert list_1 == [1, 3, 4, 1, 5, 7, 8, 10]


import pytest


def test_add_at_index_edge() -> None:
    """tests the add_at_index funtion if the list is empty"""
    with pytest.raises(IndexError):
        list_1: list[int] = [1, 3, 4, 5, 7, 8, 10]
        add_at_index(list_1, 1, -1)
