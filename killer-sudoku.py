def is_valid_killer_sudoku(grid, cages):
    # sudoku rules
    def is_valid_sudoku():
        # rows
        for row in grid:
            if len(set(row)) != 9:
                return False
        # columns
        for col in range(9):
            if len(set(grid[row][col] for row in range(9))) != 9:
                return False
        # 3x3 blocks
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                block = set()
                for r in range(3):
                    for c in range(3):
                        num = grid[box_row + r][box_col + c]
                        if num in block:
                            return False
                        block.add(num)
        return True

    # check if each cage has the correct sum and no repeated numbers
    def is_valid_cages():
        for cage in cages:
            total_sum = cage['sum']
            positions = cage['cells']
            cage_values = [grid[row][col] for row, col in positions]
            if sum(cage_values) != total_sum or len(set(cage_values)) != len(cage_values):
                return False
        return True

    # output
    if is_valid_sudoku() and is_valid_cages():
        print("The solution is valid!")
        return True
    else:
        print("The solution is not valid.")
        return False

# Proposed solution for Killer Sudoku (9x9 grid)
solution_grid = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

# Definition of cages with sum and cells
cages = [
    {'sum': 15, 'cells': [(0, 0), (0, 1), (1, 0), (1, 1)]},
    {'sum': 10, 'cells': [(0, 2), (0, 3), (1, 2)]},
    {'sum': 12, 'cells': [(0, 4), (0, 5), (1, 4)]},
    {'sum': 16, 'cells': [(0, 6), (0, 7), (1, 6)]},
    {'sum': 17, 'cells': [(0, 8), (1, 8), (2, 8)]},
    {'sum': 14, 'cells': [(1, 3), (2, 3), (3, 3)]},
    {'sum': 20, 'cells': [(1, 5), (2, 5), (3, 5)]},
    {'sum': 13, 'cells': [(2, 0), (2, 1), (3, 0)]},
    {'sum': 15, 'cells': [(2, 2), (3, 2), (4, 2)]},
    {'sum': 9,  'cells': [(4, 0), (5, 0), (6, 0)]},
]

is_valid = is_valid_killer_sudoku(solution_grid, cages)
