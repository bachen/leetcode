class Solution:
    # @param {integer[]} nums red 0 white 1 blue 2
    # @return {void} Do not return anything, modify nums in-place instead.
	def sortColors(self, nums):
		length = len(nums)
		if length > 1:
			red =  []
			white =[]
			blue = []
			for i in nums:
				if i == 0:
					red.append(i)
				elif i == 1:
					white.append(i)
				else:
					blue.append(i)
			result = red + white + blue
			for i in range(length):
				nums[i] = result[i]