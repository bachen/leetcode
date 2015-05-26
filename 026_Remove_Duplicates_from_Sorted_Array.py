class Solution:
    # @param {integer[]} nums
    # @return {integer}
	def removeDuplicates(self, nums):
		length = len(nums)
		if length == 0:
			return 0
		if length == 1:
			return 1
		count = 0
		slow = 0
		if nums[0] == nums[1]:
			mark = nums[1]
			slow = 1
		else:
			mark = nums[0]
		for i in range(1,length):
			if (nums[i] == nums[i-1]) & (slow == 0):
				count += 1
				slow = i
				mark = nums[i]
			elif (nums[i] != mark) & (slow != 0):
				nums[slow] =  nums[i]
				slow += 1
				mark = nums[i]
			elif (nums[i] == mark) & (slow != 0):
				count += 1
		for i in range(count):
			nums.pop()
		length = length - count
		return length

test = Solution()
print test.removeDuplicates([1,2,2])
