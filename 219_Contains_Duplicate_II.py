class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        length = len(nums)
        d = {}
        flag = False
        for i in range(length):
        	if d.has_key(nums[i]):
        		distance = i - d[nums[i]]
        		if k >= distance:
        			flag = True
        		else:
        			d[nums[i]] = i
        	else:
        		d[nums[i]] = i
        return flag

test = Solution()
print test.containsNearbyDuplicate([1,0,1,1],1)