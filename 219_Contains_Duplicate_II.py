class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
	def containsNearbyDuplicate(self, nums, k):
		length = len(nums)
		d = {}
		if k >= length:
			for i in nums:
				if d.has_key(i):
					return True
				else:
					d[i] = 1
			return False
		else:
			limit = k
			while (length >= limit):
				d = {}
				for i in range(limit-k,limit):
					if d.has_key(nums[i]):
						return True
					else:
						d[nums[i]] = 1
				limit += 1
			return False

test = Solution()
print test.containsNearbyDuplicate([1,2],2)