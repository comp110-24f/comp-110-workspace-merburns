"""Exercise 5"""

__author__ = "730481454"


def only_evens(input: list[int]) -> list[int]:
    """goes through a list and put all even #'s in a new list"""
    evens: list[int] = []  # makes an empty list
    for elem in input:
        if elem % 2 == 0:
            evens.append(elem)
    return evens


def sub(input: list[int], start_idx: int, end_idx: int) -> list[int]:
    """makes a list that is the subset of input between the start and end"""
    result: list[int] = []  # makes an empty list
    for idx in range(0, len(input)):
        if idx >= start_idx and idx < end_idx:  # checks for both cases
            result.append(input[idx])
    return result


def add_at_index(input: list[int], add: int, idx: int) -> None:
    """adds "add" at "idx" in the input list"""
    if idx < 0 or idx > len(input):
        raise IndexError("Index is out of bounds for the input list")
    input.append(0)
    i = len(input) - 1
    while i > idx:
        input[i] = input[i - 1]
        i -= 1
    input[idx] = add
