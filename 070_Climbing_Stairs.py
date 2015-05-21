class Solution:
    # @param {integer} n
    # @return {integer}
	def climbStairs(self, n):
		if n == 0:
			return 0
		if n == 1:
			return 1
		if n == 2:
			return 2
		nums = [1,1,2]
		for i in range(3,n+1):
			nums.append(0)
			nums[i] = nums[i-1] + nums[i-2]
		return nums[n]

	def climbStairs1(self,n): #递归，超时了
		if n == 0:
			return 0
		if n == 1:
			return 1
		if n == 2:
			return 2
		return self.climbStairs(n-1) + self.climbStairs(n-2)

test = Solution()
print test.climbStairs(35)