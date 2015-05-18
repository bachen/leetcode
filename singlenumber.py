class Solution:
    # @param {integer[]} nums
    # @return {integer}
	def singleNumber(self, nums):
		length = len(nums)
		if length == 0:
			return None
		if length == 1:
			return nums[0]
		d = {}
		for i in nums:
			if d.has_key(i):
				d.pop(i)
			else:
				d[i] = 1
		return d.keys()[0]

	def singleNumber1(self,nums):
		length = len(nums)
		if length == 0:
			return None
		if length == 1:
			return nums[0]
		x = 0
		for i in nums:
			x = x^i
		return x