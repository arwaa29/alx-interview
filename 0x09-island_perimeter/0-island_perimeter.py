#!/usr/bin/python3

class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        length_row = len(grid)
        lengt_column = len(grid[0])

        p=0
        connections = 0

        for x in range(0, length_row):
            for y in range(0, length_column):

                if grid[x][y] == 1:
                    p += 4

                    if x != 0 and grid[x-1][y] == 1:
                        connections += 1
                    if y != 0 and grid[x][y-1] == 1:
                        connections += 1
        return p - (connections*2)class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        length_row = len(grid)
        length_column = len(grid[0])

        p = 0  # Total perimeter

        for x in range(length_row):
            for y in range(length_column):

                if grid[x][y] == 1:
                    p += 4  # Start with 4 sides for each land cell

                    # Check if there's a neighboring land cell above
                    if x > 0 and grid[x-1][y] == 1:
                        p -= 2  # Subtract 2 for the shared border

                    # Check if there's a neighboring land cell to the left
                    if y > 0 and grid[x][y-1] == 1:
                        p -= 2  # Subtract 2 for the shared border

        return p

