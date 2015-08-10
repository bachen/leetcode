class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        if (m==0) | (n==0) :
        	return False
        start = 0
        end = m-1
        for i in range(m):
        	if matrix[i][0] > target:
        		end = i-1
        	if target > matrix[i][n-1]:
        		start = i+1
        if start > end:
        	return False
    	for j in range(n):
    		if matrix[start][j] == target:
    			return True
    	return False

test = Solution()
print test.searchMatrix([[-10,-9],[-7,-5]],-13)