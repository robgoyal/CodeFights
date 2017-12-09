# Name: cavityMap.py
# Author: Robin Goyal
# Last-Modified: December 8, 2017
# Purpose:


def isCavity(grid, i, j):
    '''
    grid -> list: strings indicating depths of each cell in row
    i -> int: index of cell in row
    j -> int: index of cell in column

    return -> bool: if grid[i][j] is a cavity

    A cavity is defined as every cell adjacent to it has strictly smaller depth
    '''
    try:
        return int(grid[i][j]) > int(grid[i - 1][j]) and \
            int(grid[i][j]) > int(grid[i + 1][j]) and \
            int(grid[i][j]) > int(grid[i][j - 1]) and \
            int(grid[i][j]) > int(grid[i][j + 1])

    # ValueError occurs since comparison could occur with 'X' and this would
    # indicate that the current cell has an adjacent value that is already a cavity
    except ValueError:
        return False


def cavityMap(grid):
    '''
    grid -> list: strings indicating depths of each cell in row
    return -> list: new grid with cavities replaced with X's
    '''

    new_grid = list(grid)

    # Cavity can't occur on border of grid
    for row in range(1, len(new_grid) - 1):
        for col in range(1, len(new_grid[0]) - 1):

            # Check if cell is a cavity
            if isCavity(new_grid, row, col):

                # Replace current cell with X
                new_grid[row] = new_grid[row][:col] + "X" + new_grid[row][col + 1:]

    return new_grid


def main():
    n = int(input().strip())
    grid = []

    for grid_i in range(n):
        grid_t = str(input().strip())
        grid.append(grid_t)

    result = cavityMap(grid)

    for row in result:
        print(row)


if __name__ == "__main__":
    main()
