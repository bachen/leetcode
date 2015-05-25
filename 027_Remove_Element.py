class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
	def removeElement(self, nums, val):
		length = len(nums)
		if length == 0:
			return 0
		if length == 1:
			if nums[0] == val:
				return 0
			else:
				return 1
		i = 0
		j = length - 1
		while (j >= i) & (j >= 0):
			if nums[j] == val:
				nums.pop()
				j -= 1
				continue
			if nums[i] == val:
				tmp = nums[j]
				nums[j] = nums[i]
				nums[i] = tmp
				nums.pop()
				i += 1
				j -= 1
				continue
			else:
				i += 1
		new_length = len(nums)
		return new_length,nums

test = Solution()
print test.removeElement([1,2,3,4],2)