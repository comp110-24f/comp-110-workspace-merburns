"""Challenge Question 7"""

__author__ = "730481454"


def find_and_remove_max(input: list[int]) -> int:
    """Finds the largest values and removes it from the list"""
    if len(input) == 0:
        return -1
    max_value: int = input[0]
    for elem in input:
        if elem > max_value:
            max_value = elem
    idx: int = 0
    while idx < len(input):
        if input[idx] == max_value:
            input.pop(idx)
        else:
            idx += 1
    return max_value
