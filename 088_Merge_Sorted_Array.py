class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        p1,p2,end = m-1,n-1,n+m-1
        while p1 >=0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[end] = nums2[p2]
                p2 -= 1
            else:
                nums1[end] = nums1[p1]
                p1 -= 1
            end -= 1
        if p1 < 0:
            for i in range(p2+1):
                nums1[i]=nums2[i]
        print nums1

test = Solution()
test.merge([0],0,[1],1)