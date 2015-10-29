# Definition for a binary tree node.
import Queue

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
        q = Queue.Queue(-1)
        q.put(root)
        res = serial(q,1,[])
        length = len(res)
        for i in xrange(-1,-length,-1):
            if res[-1] == 'null':
                res.pop()
            else:
                break
        return '[' + ' '.join(res) + ']'

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
        q = Queue.Queue(-1)
        q.put(root)
        deserial(q,1,nodes,1,length)
        return root

def serial(q,size,s):
    count = 0
    if size == 0:
        return s
    for i in range(size):
        node = q.get()
        if node == None:
            s.append('null')
        else:
            s.append(str(node.val))
            q.put(node.left)
            q.put(node.right)
            count += 2
    serial(q,count,s)
    return s

def deserial(q,size,nodes,loc,length):
    count = 0
    if size == 0:
        return
    if loc > length:
        return
    for i in range(size):
        node = q.get()
        if node == None:
            loc += 1
            continue
        else:
            if loc < length:
                node.left = TreeNode(nodes[loc])
                loc += 1
                q.put(node.left)
                count += 1
            else:
                return
            if loc < length:
                node.right = TreeNode(nodes[loc])
                loc += 1
                q.put(node.right)
                count += 1
            else:
                return
    deserial(q,count,nodes,loc,length)

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
#m[2].left = m[5]
m[2].right = m[6]
m[6].right = m[7]

c = Codec()
#print c.deserialize('[1]').val
print c.serialize(m[0])