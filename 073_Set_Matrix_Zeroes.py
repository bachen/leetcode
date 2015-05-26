class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
	def setZeroes(self, matrix):
		row = len(matrix)
		column = len(matrix[0])

		for i in range(row):
			if matrix[i][0] == 0:
				row_0 = True
				break
			else:
				row_0 = False
		for j in range(column):
			if matrix[0][j] == 0:
				column_0 = True
				break
			else:
				column_0 = False
		for i in range(row):
			for j in range(column):
				if matrix[i][j] == 0:
					if matrix[i][0] != 0:
						matrix[i][0] = 0
					if matrix[0][j] != 0:
						matrix[0][j] = 0
		for j in range(1,column):
			if matrix[0][j] == 0:
				for i in range(row):
					matrix[i][j] = 0
		for i in range(1,row):
			if matrix[i][0] == 0:
				matrix[i] = [0]*column
		if row_0 == True:
			for i in range(row):
				matrix[i][0] = 0
		if column_0 == True:
			matrix[0] = [0]*column

test = Solution()
m = [[1,1,1],[0,1,2]]
test.setZeroes(m)
print m
print 