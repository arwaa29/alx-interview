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
        return p - (connections*2)
