#!/usr/bin/python3
"""
This module contains the function that solves the lockboxes challenge
"""


def canUnlockAll(boxes):
    """
       Determines if all the boxes can be opened

       Args:
            boxes ((List[List[int]])): A list of lists of boxes
       Return: True if all boxes can be opened ELSE, return False
    """
    visited_indexes = set()
    iterate_over_boxes(boxes, 0, visited_indexes)
    return len(visited_indexes) == len(boxes)


def iterate_over_boxes(boxes, index, visited_indexes):
    """
        Recursively iterates over the boxes from a given index while keeping
        track of the visited indexes

        Args:
            boxes (List[List[int]]): A list of lists of boxes
            index (int): The index to currently stat the box iteration.
            visited_indexes (set): A set visited box indexes.

        Returns:
            visited_indexes (set): A set containing all visited indexes
    """
    if index in visited_indexes:
        return

    visited_indexes.add(index)

    for key in boxes[index]:
        if key < len(boxes):
            iterate_over_boxes(boxes, key, visited_indexes)
