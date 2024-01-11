#!/usr/bin/python3
'''
Module that solves the N Queens puzzle
'''
from sys import argv, exit


if __name__ == "__main__":
    if len(argv) != 2:
        print('Usage: nqueens N')
        exit(1)
    try:
        n = int(argv[1])
    except BaseException:
        print('N must be a number')
        exit(1)
    if n < 4:
        print('N must be at least 4')
        exit(1)

    queens_positions = []

    def solve_queens(row, n, queens_positions):
        if row == n:
            print(queens_positions)
        else:
            for col in range(n):
                current_placement = [row, col]
                if is_valid_placement(queens_positions, current_placement):
                    queens_positions.append(current_placement)
                    solve_queens(row + 1, n, queens_positions)
                    queens_positions.remove(current_placement)

    def is_valid_placement(queens_positions, current_placement):
        for queen in queens_positions:
            if queen[1] == current_placement[1]:
                return False
            if (queen[0] + queen[1]) == (current_placement[0] + current_placement[1]):
                return False
            if (queen[0] - queen[1]) == (current_placement[0] - current_placement[1]):
                return False
        return True

    solve_queens(0, n, queens_positions)
