#!/usr/bin/python3

def island_perimeter(grid):
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # land cell
                # Check each side of the cell
                # Top
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # Bottom
                if i == rows-1 or grid[i+1][j] == 0:
                    perimeter += 1
                # Left
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # Right
                if j == cols-1 or grid[i][j+1] == 0:
                    perimeter += 1
    
    return perimeter

