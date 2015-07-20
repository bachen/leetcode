# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
	def invertTree(self, root):
		if root == None:
			return root
		exchange(root)
		return root

def exchange(root):
	if root == None:
		return
	tmp = root.left
	root.left = root.right
	root.right = tmp
	exchange(root.left)
	exchange(root.right)

s = [1,2,3,4,5,6,7]
t0 = TreeNode(s[0])
t1 = TreeNode(s[1])
t2 = TreeNode(s[2])
t3 = TreeNode(s[3])
t4 = TreeNode(s[4])
t5 = TreeNode(s[5])
t6 = TreeNode(s[6])
t0.left = t1
t0.right = t2
t1.left = t3
t1.right = t4
t2.left = t5
t2.right = t6
print t0.right.val
print t0.right.right.val
test = Solution()
test.invertTree(t0)
print t0.right.val
print t0.right.right.val