class Solution:
	def rob(self,nums):
		length = len(nums)
		if length == 0:
			return 0
		if length == 1:
			return nums[0] 
		
		