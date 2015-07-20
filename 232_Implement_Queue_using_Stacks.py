class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stack1.append(x)

    # @return nothing
    def pop(self):
        length2 = len(self.stack2)
        if length2 != 0:
            return self.stack2.pop()
        else:
            length1 = len(self.stack1)
            for i in range(length1):
                tmp = self.stack1.pop()
                self.stack2.append(tmp)
            return self.stack2.pop()
        
    # @return an integer
    def peek(self):
        length2 = len(self.stack2)
        if length2 != 0:
            return self.stack2[-1]
        else:
            return self.stack1[0]

    # @return an boolean
    def empty(self):
        length2 = len(self.stack2)
        if length2 != 0:
            return False
        length1 = len(self.stack1)
        if length1 != 0:
            return False
        else:
            return True

test = Queue()
test.push(1)
test.push(2)
test.push(3)
print test.pop()
print test.peek()
test.push(4)
test.push(5)
print test.pop()
print test.pop()
print test.peek()
print test.pop()
print test.pop()