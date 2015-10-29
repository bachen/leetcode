# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return "[null]"
        res = serial(left,right,[str(root.val)])
        length = len(res)
        if length == (2**(length/2)-1):
            return '['+ ' '.join(res) +']'
        else:
            for i in range(length):
                if res[-1] == 'null':
                    res.pop()
            return '['+ ' '.join(res) +']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if (data == '[]') | (data == '[null]'):
            return None
        data = data.split('[')[1]
        data = data.split(']')[0]
        nodes = data.split(' ')
        length = len(nodes)
        root = TreeNode(nodes[0])
        deserial(root,nodes,1,length)
        return root

def serial(left,right,s):
    if (left == None) & (right == None):
        s.append('null')
        s.append('null')
    elif (left != None) & (right == None):
        s.append(str(left.val))
        s.append('null')
        serial(left.left,left.right,s)
    elif (root.left == None) & (root.right != None):
        s.append('null')
        s.append(str(root.right.val))
        serial(root.right,s)
    else:
        s.append(str(root.left.val))
        s.append(str(root.right.val))
        serial(root.left,s)
        serial(root.right,s)
    return s

def deserial(root,nodes,count,length):
    if count >= length:
        return
    if nodes[count] != 'null':
        root.left = TreeNode(nodes[count])
    count += 1
    if count >= length:
        return
    if nodes[count] != 'null':
        root.right = TreeNode(nodes[count])
    count += 1
    if count >= length:
        return
    if root.left != None:
        deserial(root.left,nodes,count,length)
        count += 2
    if count >= length:
        return
    if root.right != None:
        deserial(root.right,nodes,count,length)
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

m = []
for i in range(9):
    m.append(TreeNode(i))
m[0].left = m[1]
m[0].right = m[2]
m[1].left = m[3]
m[1].right = m[4]
m[2].left = m[5]
m[2].right = m[6]

c = Codec()
print c.deserialize('[1 2 3 4 5 6 7 8 9 10]').left.left.left.val
#print c.serialize(m[0])