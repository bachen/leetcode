# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
	def postorderTraversal(self, root):
		if root == None:
			return []
		result = []
		result = gettree(root,result)
		return result

def gettree(root,result):
	if root == None:
		return result
	if root.left != None:
		gettree(root.left,result)
	if root.right != None:
		gettree(root.right,result)
	result.append(root.val)
	return result

test =Solution()
s = []
for i in range(3):
	s.append(TreeNode(i))
s[0].right = s[1]
s[1].left = s[2]
print test.postorderTraversal(s[0])