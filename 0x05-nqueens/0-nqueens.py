#!/usr/bin/python3
"""
This  module contains the solution for the N-Queens problem
"""
import sys
from typing import List


class NQueens:
    def __init__(self):
        """
        Initialize a new NQueens solution instance.
        """
        if len(sys.argv) != 2:
            print("Usage: nqueens N")
            sys.exit(1)
        try:
            self.n = int(sys.argv[1])
        except ValueError:
            print("N must be a number")
            sys.exit(1)

        if self.n < 4:
            print("N must be at least 4")
            sys.exit(1)
        self.solutions: List[List[int]] = []

    def run(self):
        """Runs the NQueens solution."""
        self.solve([], [], [])
        self.display_solution()

    def solve(self, queens: List[int], diff_of_xy: List[int], sum_of_xy: List[int]):
        """
        Solves the NQueens problem recursively.

        Args:
            queens (list): the positions of the queens on the board
            diff_of_xy (list): the differences of the positions of the queens
            sum_of_xy (list): the sums of the positions of the queens
        """
        if len(queens) == self.n:
            self.solutions.append(list(queens))
            return

        for i in range(self.n):
            if (
                    i in queens
                    or (len(queens) - i) in diff_of_xy
                    or (len(queens) + i) in sum_of_xy
            ):
                continue

            self.solve(
                queens + [i],
                diff_of_xy + [len(queens) - i],
                sum_of_xy + [len(queens) + i],
            )

    def display_solution(self):
        """
        Displays the NQueens solution.
        """
        for j in self.solutions:
            print([[i, j[i]] for i in range(self.n)])


if __name__ == "__main__":
    x = NQueens()
    x.run()
