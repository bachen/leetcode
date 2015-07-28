# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def countNodes(self, root):
    	if root == None:
    		return 0
        left = get_left(root)+1
        right = get_right(root)+1
        if (left == right):
        	return (2<<(left-1))-1
        else:
        	return self.countNodes(root.left) + self.countNodes(root.right) + 1

def get_left(root):
    count = 0
    while(root.left):
    	count += 1
    	root = root.left
    return count

def get_right(root):
    count = 0
    while(root.right):
    	count += 1
    	root= root.right
    return count

t0 = TreeNode(0)
t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t6 = TreeNode(6)
t7 = TreeNode(7)
t8 = TreeNode(8)

t0.left = t1
t0.right = t2
'''
t1.left = t3
t1.right = t4
t2.left = t5
t2.right = t6
t3.left = t7
t3.right = t8
'''
test = Solution()
print test.countNodes(t0)