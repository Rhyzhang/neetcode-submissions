class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        perimeter = 0

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if grid[i][j] == 1:
                    # check right
                    try:
                        if grid[i][j+1] == 0:
                            perimeter += 1
                    except:
                        perimeter += 1

                    # check bottom
                    try:
                        if grid[i+1][j] == 0:
                            perimeter += 1
                    except:
                        perimeter += 1
                    
                    # check top
                    try:
                        if i-1 < 0:
                            raise ValueError("Numbers must be non-negative")
                        if grid[i-1][j] == 0:
                            perimeter += 1
                    except:
                        perimeter += 1

                    # check left
                    try:
                        if j-1 < 0:
                            raise ValueError("Numbers must be non-negative")
                        if grid[i][j-1] == 0:
                            perimeter += 1
                    except:
                        perimeter += 1
        return perimeter

        