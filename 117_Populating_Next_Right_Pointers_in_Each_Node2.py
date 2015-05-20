# Definition for binary tree with next pointer.
class TreeLinkNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
		if root == None:
			return None
		if (root.left == None) & (root.right == None):
			return None
		elif (root.left != None) & (root.right != None):
			left = root.left
			right = root.right
			left.next = right
			getresult(left)
		else:
			getresult(root)

def getresult(root):
	if (root != None):
		left = root.left
		right = root.right
		new_root = None
		node = None
		#首先找到下一行的起始new_root和本行进行connect的起始node
		if (left != None) & (right != None):
			new_root = left
			left.next = right
			node = right
		elif (right != None):
			new_root = right
			node = right
		elif (left != None):
			new_root = left
			node = left
		else:  #如果出现左子树为空的情况，需要root.next向右寻找合适的下一行的起始new_root和本行进行connect的起始node
			while root.next:
				root = root.next
				left = root.left
				right = root.right
				if (left != None) & (right != None):
					new_root = left
					left.next = right
					node = right
					break
				elif (right != None):
					new_root = right
					node = right
					break
				elif (left != None):
					new_root = left
					node = left
					break
				else:
					continue  #继续向右查找
			if (new_root == None) & (node == None): #如果root.next==None，且始终未找到new_root和node，那么视为递归结束
				return None
		while root.next:
			root = root.next
			if (root.left == None) & (root.right == None):
				continue
			elif (root.left != None) & (root.right != None):
				node.next = root.left
				node = root.right
				left = root.left
				left.next = node
			elif (root.left == None) & (root.right != None):
				node.next = root.right
				node = root.right
			else:
				node.next = root.left
				node = root.left
		getresult(new_root)
	else:
		return None

s =[]
for i in range(7):
	s.append(TreeLinkNode(i))
s[0].right = s[2]
s[0].left = s[1]
#s[1].right = s[4]
#s[1].left = s[3]
s[2].right = s[6]
s[2].left = s[5]

test = Solution()
test.connect(s[0])
print s[1].next.val
print s[5].next.val