# Killer Sudoku Validator

This project is a Python-based solution checker for Killer Sudoku puzzles. It verifies whether a provided solution satisfies the requirements of a standard Sudoku puzzle as well as the additional constraints specific to Killer Sudoku.

## Table of Contents

- [What is Sudoku?](#what-is-sudoku)
- [What is Killer Sudoku?](#what-is-killer-sudoku)
- [Project Overview](#project-overview)
- [How It Works](#how-it-works)
- [Example Usage](#example-usage)

## What is Sudoku?

Sudoku is a logic-based, combinatorial number-placement puzzle. The classic Sudoku grid consists of a 9x9 grid that is subdivided into nine 3x3 subgrids, often called "boxes." The goal is to fill each cell of the grid with a number from 1 to 9 so that each number appears exactly once in each row, column, and 3x3 box. Sudoku puzzles start with some numbers pre-filled, and the difficulty of the puzzle generally increases as fewer numbers are provided at the start.

## What is Killer Sudoku?

Killer Sudoku is a variation of the classic Sudoku puzzle that combines elements of Sudoku and Kakuro. In addition to the standard Sudoku rules, Killer Sudoku has additional regions, known as "cages," that impose a specific sum constraint. Each cage contains a group of cells with a total sum that is predefined. Additional rules for Killer Sudoku include:
1. Each cage has a specified sum, and the numbers in that cage must add up to that sum.
2. No number may repeat within a cage, even if it does not violate Sudoku's standard row, column, or box constraints.

These additional constraints make Killer Sudoku a more challenging puzzle, as players must consider both the placement and the sum conditions simultaneously.

## Project Overview

This project contains Python code that checks if a given solution for a Killer Sudoku puzzle is valid. The program performs the following checks:
1. **Standard Sudoku Validation**: Verifies that each row, column, and 3x3 box contains numbers from 1 to 9 with no repetitions.
2. **Cage Sum and Uniqueness Check**: Verifies that each cage in the puzzle has the correct sum and that no numbers are repeated within any cage.

## How It Works

The program is structured with the following key functions:

- **`is_valid_sudoku()`**: Checks that the solution adheres to the rules of a standard Sudoku puzzle by validating each row, column, and 3x3 box.
- **`is_valid_cages()`**: Checks that each cage in the Killer Sudoku puzzle satisfies the specified sum and contains no duplicate numbers.
- **`is_valid_killer_sudoku()`**: Combines the results of `is_valid_sudoku()` and `is_valid_cages()` to determine if the solution meets all Killer Sudoku requirements.

The program uses a 9x9 grid (a list of lists) for the Sudoku solution and a list of dictionaries for the cages. Each dictionary includes:
- **`sum`**: The target sum for the cage.
- **`cells`**: A list of (row, column) tuples representing the cells in the cage.

If both the Sudoku rules and cage rules are satisfied, the solution is valid.

## Example Usage

Here is an example of how to use the program to validate a solution:

```python
solution_grid = [
    [4, 3, 5, 2, 6, 9, 7, 8, 1],
    [6, 8, 2, 5, 7, 1, 4, 9, 3],
    [1, 9, 7, 8, 3, 4, 5, 6, 2],
    [8, 2, 6, 1, 9, 5, 3, 4, 7],
    [3, 7, 4, 6, 8, 2, 9, 1, 5],
    [9, 5, 1, 7, 4, 3, 6, 2, 8],
    [5, 1, 9, 3, 2, 6, 8, 7, 4],
    [2, 4, 8, 9, 5, 7, 1, 3, 6],
    [7, 6, 3, 4, 1, 8, 2, 5, 9]
]

cages = [
    {'sum': 15, 'cells': [(0, 0), (0, 1), (1, 0), (1, 1)]},
    {'sum': 9,  'cells': [(0, 2), (1, 2), (2, 2)]},
    {'sum': 17, 'cells': [(0, 3), (0, 4), (1, 3), (1, 4)]},
    {'sum': 14, 'cells': [(0, 5), (0, 6), (1, 5)]},
    {'sum': 23, 'cells': [(1, 6), (1, 7), (2, 6), (2, 7)]},
    {'sum': 15, 'cells': [(2, 0), (2, 1), (3, 0)]},
    {'sum': 12, 'cells': [(2, 3), (2, 4), (3, 3)]},
    {'sum': 18, 'cells': [(3, 4), (4, 4), (5, 4)]},
    {'sum': 17, 'cells': [(4, 0), (4, 1), (5, 0), (5, 1)]},
    {'sum': 13, 'cells': [(6, 0), (6, 1), (7, 0), (8, 0)]}
]

is_valid = is_valid_killer_sudoku(solution_grid, cages)
print("Is the solution valid?", is_valid)
