class Solution:
    # @param {integer[]} nums
    # @return {integer}
	def majorityElement(self, nums):
		majority_index = 0
		count = 1
		length = len(nums)
		for i in range(1,length):
			if nums[majority_index] == nums[i]:
				count += 1
			else:
				count -= 1
			if count == 0:
				majority_index = i
				count = 1
		return nums[majority_index]

	def majorityElement1(self, nums):
		d = {}
		if nums == []:
			return None
		length = len(nums)
		mark = length/2
		for i in nums:
			if d.has_key(i):
				d[i] += 1
			else:
				d[i] = 1
		max_num = 0
		mark = length/2
		major_em = nums[0]
		for k,v in d.items():
			if (v > max_num) and (v > mark):
				max_num = v
				major_em = k
		return major_em

test = Solution()
print test.majorityElement([1,1,1,2,3,4,5,5,5,5,5,5,5])