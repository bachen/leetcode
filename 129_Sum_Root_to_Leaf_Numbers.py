# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sum(self, root, preSum):
        if root==None: 
            return 0
        preSum = preSum*10 + root.val
        if root.left==None and root.right==None: 
            return preSum
        return self.sum(root.left, preSum)+self.sum(root.right, preSum)
        
    def sumNumbers(self, root):
        return self.sum(root, 0)

t0 = TreeNode(4)
t1 = TreeNode(0)
t2 = TreeNode(9)
t3 = TreeNode(1)

t0.left = t1
t0.right = t2
t2.right = t3

s0 = TreeNode(1)
s1 = TreeNode(2)
s2 = TreeNode(3)
s0.left = s1
s0.right = s2

test = Solution()
print test.sumNumbers(t0)
print test.sumNumbers(s0)
