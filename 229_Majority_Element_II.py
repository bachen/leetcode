class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
	def majorityElement(self, nums):
		length = len(nums)
		if length < 2:
			return nums
		thres = length/3
		d = {}
		for i in range(length):
			if d.has_key(nums[i]):
				d[nums[i]] += 1
			else:
				d[nums[i]] = 1
		result = []
		for k,v in d.items():
			if v > thres:
				result.append(k)
		return result

test = Solution()
print test.majorityElement([1,2,3,1,2,3,4,5,1,2,1,2,1,2])