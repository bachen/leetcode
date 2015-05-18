class Solution:
	# @param {integer[]} nums
	# @param {integer} target
	# @return {integer[]}
	def twoSum(self, nums, target):
		left = []
		length = len(nums)
		left_length = 0
		if length <= 0:
			return 0
		for i in range(length):
			tmp = target - nums[i]
			if nums[i] not in left:
				left.append(tmp)
				#print left
			else:
				return (left.index(nums[i])+1,i+1)

	def twoSum1(self, nums, target):
		left = {}
		length = len(nums)
		left_length = 0
		if length <= 0:
			return 0
		for i in range(length):
			tmp = target - nums[i]
			if left.get(nums[i]) != None:
				return (left.get(nums[i])+1,i+1)
			else:
				left[tmp] = i
				print left

test = Solution()
print test.twoSum1([0,7,3,4,11,0],0)