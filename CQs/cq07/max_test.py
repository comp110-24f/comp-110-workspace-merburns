__author__ = "730481454"

from CQs.cq07.find_max import find_and_remove_max


# test for the use case, return
def test_return() -> None:
    """runs the function to see if the return value is correct"""
    ran_num: list[int] = [0, 6, 11, 4, 7, 8, 10, 11]
    assert find_and_remove_max(ran_num) == 11


# test for use case, mutate
def test_max_removed() -> None:
    """runs the function and sees if the function mutates the list in the correct way"""
    ran_num: list[int] = [0, 6, 11, 4, 7, 8, 10, 11]
    find_and_remove_max(ran_num)
    assert ran_num == [0, 6, 4, 7, 8, 10]


# test for an edge case, when list is empty
def test_edge() -> None:
    """run the function and sees if -1 is the result"""
    ran_num: list[int] = []
    assert find_and_remove_max(ran_num) == -1
