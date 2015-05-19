class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
	def threeSum(self, nums):
		length = len(nums)
		if length <= 2:
			return []
		nums.sort()
		if length == 3:
			if (nums[0]+nums[1]+nums[2]) == 0:
				return [nums]
			else:
				return []
		result = []
		#print nums
		m = 0
		while(m < (length-2)):
			i = m + 1
			j = length - 1
			target = 0 - nums[m]
			while( j > i ):
				sum2 = nums[j] + nums[i]
				if sum2 == target:
					tmp = [nums[m],nums[i],nums[j]]
					#print tmp
					result.append(tmp)
					while ((j>i)&(nums[j]==nums[j-1])):
						j -= 1
					while((j>i)&(nums[i]==nums[i+1])):
						i += 1
					i += 1
					j -= 1
				elif sum2 > target:
					j -= 1
				else:
					i += 1
			while((m<(length-2)) & (nums[m]==nums[m+1])):
				m += 1
			m += 1
		return result

test = Solution()
#print test.threeSum([0,0,0,0])
print test.threeSum([12,13,-10,-15,4,5,-8,11,10,3,-11,4,-10,4,-7,9,1,8,-5,-1,-9,-4,3,-14,-11,14,0,-8,-6,-2,14,-9,-4,11,-8,-14,-7,-9,4,10,9,9,-1,7,-10,7,1,6,-8,12,12,-10,-7,0,-9,-3,-1,-1,-4,8,12,-13,6,-7,13,5,-14,13,12,6,8,-2,-8,-15,-10,-3,-1,7,10,7,-4,7,4,-4,14,3,0,-10,-13,11,5,6,13,-4,6,3,-13,8,1,6,-9,-14,-11,-10,8,-5,-6,-7,9,-11,7,12,3,-4,-7,-6,14,8,-1,8,-4,-11])