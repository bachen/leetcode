class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
	def rotate(self, matrix):
		n = len(matrix)
		middle = n/2
		if n > 1:
			for i in range(0,middle+1):
				for j in range(i,n-1-i):
					tmp = matrix[i][j]
					matrix[i][j] = matrix[n-1-j][i]
					matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
					matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
					matrix[j][n-1-i] = tmp

test = Solution()
m = [[1,1],[2,2]]
test.rotate(m)
print m