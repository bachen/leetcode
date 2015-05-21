class Solution:
    # @param {integer} n
    # @return {integer}
	def numTrees(self, n):
		if n == 0:
			return 0
		if n == 1:
			return 1
		if n == 2:
			return 2
		nums = [1,1,2]
		for i in range(3,n+1):
			if (i >= 3):
				nums.append(0)
				for j in range(1,i+1):
					nums[i] += nums[j-1]*nums[i-j]
		return nums[n]

test = Solution()
print test.numTrees(5)