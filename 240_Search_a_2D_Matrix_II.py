class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        width = len(matrix)
        length = len(matrix[0])
        w_start = 0
        w_end = width - 1
        for i in range(width):
        	if (matrix[w_start][length-1] < target):
        		w_start += 1
        	if (matrix[w_end][0] > target):
        		w_end -= 1
        flag = False
        print w_start,w_end
        for i in range(w_start,w_end+1):
        	for j in range(length):
        		if (matrix[i][j] == target):
        			flag = True
        return flag

test = Solution()
print test.searchMatrix([[1,3,4,6,12],[3,6,15,17,23],[5,8,9,15,25],[25,38,39,45,55]],23)