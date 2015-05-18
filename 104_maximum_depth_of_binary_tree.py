# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
	def maxDepth(self, root):
		if root == None:
			return 0
		else:
			return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))

test = Solution()
vallist = [1,3,5,7,9,2,4]
t = []
for i in vallist:
	t.append(TreeNode(i))
t[0].left = t[1]
t[0].right = t[2]
t[1].right = t[4]
t[2].left = t[5]
t[3].right = t[6]

print test.maxDepth(t[0])