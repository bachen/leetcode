class Solution:
    # @param {integer[][]} grid
    # @return {integer}
	def minPathSum(self, grid):
		m = len(grid)
		if m == 0:
			return 0
		n = len(grid[0])
		if n == 0:
			return 0
		if (m==1)&(n==1):
			return grid[0][0]
		res = [[0 for j in range(n)] for i in range(m)]
		res[0][0]=grid[0][0]
		for i in range(m):
			res[i][0] = res[i-1][0]+grid[i][0]
		for j in range(n):
			res[0][j] = res[0][j-1]+grid[0][j]
		for i in range(1,m):
			for j in range(1,n):
				res[i][j] = min(res[i-1][j],res[i][j-1])+grid[i][j]
		return res[m-1][n-1]

test = Solution()
print test.minPathSum([[1,3,1],[2,3,1]])