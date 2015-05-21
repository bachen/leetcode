# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {integer[]} nums
    # @return {TreeNode}
    def sortedArrayToBST(self, nums):
    	if nums == []:
			return None
		length = len(nums)
		if length == 1:
			root = TreeNode(nums[0])
			return root
		#nums = nums[::-1]
		if length == 2:
			root = TreeNode(nums[0])
			root.left = TreeNode(nums[1])
			return root
		middle = length/2
		root = TreeNode(nums[middle])
		gettree(nums,0,length-1)
		return root

def gettree(nums,start,end):
	middle = (end - start)/2
	

	def sortedArrayToBST1(self, nums):
		if nums == []:
			return None
		length = len(nums)
		if length == 1:
			root = TreeNode(nums[0])
			return root
		#nums = nums[::-1]
		if length == 2:
			root = TreeNode(nums[0])
			root.left = TreeNode(nums[1])
			return root
		root = TreeNode(nums[0])
		root.left = TreeNode(nums[1])
		root.right = TreeNode(nums[2])
		old_nodelist = []
		new_nodelist = [root]
		row = 1
		left = length - 3
		if left == 0:
			return root
		i = 3
		count = 2
		while (i < length):
			old_nodelist = new_nodelist
			new_nodelist = []
			if left > 2**row:
				for j in range(2**row):
					new_nodelist.append(TreeNode(i))
					i += 1
				left = left - 2**row
				count = 2**row
			else:
				for j in range(left):
					new_nodelist.append(TreeNode(i))
					i += 1
				count = left
			j = 0
			for node in old_nodelist:
				if j > count - 1:
					break
				node.left = new_nodelist[j]
				j += 1
				if j > count - 1:
					break
				node.right = new_nodelist[j]
				j += 1
		return root
