class Solution:
    # @param {integer[]} nums
    # @return {integer}
	def maxSubArray(self, nums):
		max_sum = nums[0]
		cur_sum = 0
		length = len(nums)
		if length == 0:
			return None
		if length == 1:
			return max_sum
		for i in nums:
			cur_sum += i
			#print cur_sum
			if cur_sum > max_sum:
				max_sum = cur_sum
			if cur_sum < 0:
				cur_sum = 0
				continue
		return max_sum

s0 = [-2,1,-3,4,-1,2,1,-5,4]
s1 = [-3,-2,0,-1]
test = Solution()
print test.maxSubArray(s0)
print test.maxSubArray(s1)
