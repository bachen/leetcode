class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
    	length = len(nums)
    	if 3 >= length:
    		return max(nums)
    	else:
        	return max(robb(nums[:length-1]),robb(nums[1:length]))

def robb(nums):
	length = len(nums)
	pre,now = nums[0],max(nums[0],nums[1])
	for i in range(2,length):
		now,pre = max(nums[i]+pre,now),now
	return now

test = Solution()
print test.rob([2,3,4,10,9,3])