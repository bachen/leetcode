class Solution:
    # @param {integer[][]} grid
    # @return {integer}
	def minPathSum(self, grid):
		m = len(grid)
		n = len(grid[0])
		for i in range(m):
			
