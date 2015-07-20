class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
		length = len(nums)
		if length == 0:
			return []
		if length == 1:
			return [str(nums[0])]
		result = []
		count = 0
		r1 = nums[0]
		i = 0
		while True:
			if nums[i+1] == (nums[i]+1):
				r2 = nums[i+1]
				count += 1
			elif (count == 0):
				result.append(str(r1))
				r1=nums[i+1]
			elif (count != 0):
				result.append(str(r1)+'->'+str(r2))
				r1 = nums[i+1]
				count = 0
			i += 1
			if i > length-2:
				if nums[length-1] != (nums[length-2]+1):
					result.append(str(nums[length-1]))
				else:
					result.append(str(r1)+'->'+str(nums[length-1]))
				break
		return result

test = Solution()
print test.summaryRanges([-2,0,1,2,4,5,7,8,10,11,12,14])