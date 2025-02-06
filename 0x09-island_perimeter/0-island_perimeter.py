#!/usr/bin/python3

def island_perimeter(grid):
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Start with 4 sides for each land cell
                perimeter += 4

                # Subtract 2 if the land cell has a neighbor above
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

                # Subtract 2 if the land cell has a neighbor to the left
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeterclass Solution:
    """
    This class provides a solution to calculate the perimeter of an island
    in a grid, where 0 represents water and 1 represents land.
    """

    def islandPerimeter(self, grid: list[list[int]]) -> int:
        """
        Calculates the perimeter of the island in a grid of integers.
        
        Parameters:
        grid (list[list[int]]): A list of lists of integers representing the grid.
            0 represents water, and 1 represents land. Cells are connected 
            horizontally or vertically (not diagonally).

        Returns:
        int: The perimeter of the island.

        The grid is completely surrounded by water, and there is only one island.
        The island does not contain any lakes (water that is not connected to 
        the water surrounding the island).
        """

        length_row = len(grid)
        length_column = len(grid[0])

        perimeter = 0  # Total perimeter of the island

        for x in range(length_row):
            for y in range(length_column):

                if grid[x][y] == 1:
                    perimeter += 4  # Start with 4 sides for each land cell

                    # Check if there's a neighboring land cell above
                    if x > 0 and grid[x - 1][y] == 1:
                        perimeter -= 2  # Subtract 2 for the shared border

                    # Check if there's a neighboring land cell to the left
                    if y > 0 and grid[x][y - 1] == 1:
                        perimeter -= 2  # Subtract 2 for the shared border

        return perimeter

