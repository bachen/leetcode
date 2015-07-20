class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer[]}
	def maxSlidingWindow(self, nums, k):
		length = len(nums)
		if length == 0:
			return []
		if k >= length:
			return [max(nums)]
		result = []
		move_length = length-k+1
		i = 0
		while(move_length > i):
			#print nums[i:i+k]
			result.append(max(nums[i:i+k]))
			i += 1
		return result

test = Solution()
print test.maxSlidingWindow([1,3,-1,-3,5,3,6,7],3)