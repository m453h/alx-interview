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
    visited_indexes, indexes_to_visit = set(), {0}
    total_boxes = len(boxes)

    while indexes_to_visit:
        current_index = indexes_to_visit.pop()
        visited_indexes.add(current_index)

        for index in boxes[current_index]:
            if index < total_boxes and index not in visited_indexes:
                indexes_to_visit.add(index)

    return len(visited_indexes) == total_boxes
