class Solution:
	def findMedianSortedArrays(self, nums1, nums2):
		m = len(nums1)
		n = len(nums2)
		limit = int((m+n)/2)
		flag = (m+n)%2
		count = 0
		if (m == 0) & (n == 0):
			return None
		elif m == 0:
			if flag == 0:
				return (nums2[limit] + nums2[limit - 1])/2.0
			else:
				return nums2[limit]/1.0
		elif n == 0:
			if flag == 0:
				return (nums1[limit] + nums1[limit - 1])/2.0
			else:
				return nums1[limit]/1.0
		else:
			nums = []
			while (count <= limit):
				if nums1 == []:
					if nums2 == []:
						break
					else:
						while (count <= limit):
							nums.append(nums2.pop())
							count += 1
						break
				else:
					if nums2 == []:
						while  (count <= limit):
							nums.append(nums1.pop())
							count += 1
						break
					else:
						if nums1[-1] >= nums2[-1]:
							nums.append(nums1.pop())
							count += 1
						else:
							nums.append(nums2.pop())
							count += 1
			if flag == 0:
				return (nums[limit] + nums[limit - 1])/2.0
			else:
				return nums[limit]/1.0

test = Solution()
s1 = [1,2,3,4]
s2 = [1]
print test.findMedianSortedArrays(s1,s2)