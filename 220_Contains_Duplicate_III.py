class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
	def containsNearbyAlmostDuplicate(self, nums, k, t):
		length = len(nums)
		if k >= length:
			tmp = sorted(nums)
			for i in range(1,length):
				if t >= (tmp[i] - tmp[i-1]):
					return True
			return False
		else:
			limit = k
			tmp = sorted(nums[limit-k:limit])
			for i in range(1,limit):
				if t >= (tmp[i] - tmp[i-1]):
					return True
			while (length >= limit):
				limit += 1
			return False 

test = Solution()
print test.containsNearbyAlmostDuplicate([1,0,1,1],1,1)