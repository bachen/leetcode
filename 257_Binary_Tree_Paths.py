# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if root == None:
        	return []
        if (root.right == None) & (root.left == None):
        	return [str(root.val)]
        res = []
        res = create_res(root,res,'')
        return res

def create_res(root,res,path):
	if (root.right == None) & (root.left == None):
		return res.append(path + str(root.val))
	if (root.right != None):
		create_res(root.right,res,path+str(root.val)+'->')
	if (root.left != None):
		create_res(root.left,res,path+str(root.val)+'->')
	return res

test = Solution()

s0 = TreeNode(0)
s1 = TreeNode(1)
s2 = TreeNode(2)
s3 = TreeNode(3)
s4 = TreeNode(4)

s0.right = s1
s0.left = s2
s1.left = s3
s2.right = s4
print test.binaryTreePaths(s0)