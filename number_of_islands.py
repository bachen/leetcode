grid = []

class Solution:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
        if len(grid) == 0:
        	return 0
        if len(grid[0]) == 0:
        	return 0
        	