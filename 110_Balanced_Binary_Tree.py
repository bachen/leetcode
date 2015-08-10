# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
    	if root == None:
    		return True
    	h_left = get_height(root.left,0)
    	h_right = get_height(root.right,0)
    	#print h_right,h_left
        if abs(h_left - h_right) > 1:
        	return False
        return (self.isBalanced(root.left) & self.isBalanced(root.right))

def get_height(root,h):
	if root == None:
		return 0 
	h1 = get_height(root.left,h)
	h2 = get_height(root.right,h)
	return 1+max(h1,h2)

root = TreeNode(0)
l1 = TreeNode(1)
l2 = TreeNode(2)
l3 = TreeNode(3)
l4 = TreeNode(4)
l5 = TreeNode(5)
l6 = TreeNode(5)
root.left = l1
'''
l1.left = l2
l1.right = l3
l3.left = l4
l4.left = l5
l5.left = l6

r1 = TreeNode(5)
r2 = TreeNode(5)
r3 = TreeNode(5)
root.right = r1
r1.left = r2
r1.right = r3
'''
test = Solution()
print test.isBalanced(root)