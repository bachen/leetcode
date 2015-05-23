class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
	def uniquePaths(self, m, n):
		paths = [[0,1]]
		if (m == 1) | (n == 1):
			return 1
		if m == 2:
			return n
		if n == 2:
			return m
		for i in range(1,m):
			paths.append([1,i+1])
		for j in range(2,n):
			for i in range(m):
				if i == 0:
					paths[i].append(1)
				elif i == 1:
					paths[i].append(j+1)
				else:
					add_sum = paths[i-1][j] + paths[i][j-1]
					paths[i].append(add_sum)
		print paths
		return paths[m-1][n-1]
				
test = Solution()
print test.uniquePaths(4,4)
