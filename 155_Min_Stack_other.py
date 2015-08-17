class MinStack:
    # initialize your data structure here.
    def __init__(self):
        self.s = []
        self.min = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.s.append(x)
        if (self.min == []):
            self.min.append(x)
        elif (self.min[-1] > x):
            self.min.append(x)
        else:
            tmp = self.min[-1]
            self.min.append(tmp)
            
    # @return nothing
    def pop(self):
        self.s.pop()
        self.min.pop()

    # @return an integer
    def top(self):
        if self.s == []:
            return None
        return self.s[-1]

    # @return an integer
    def getMin(self):
        if self.s == []:
            return None
        return self.min[-1]

test = MinStack()
test.push(8)
print test.getMin()
test.push(7)
print test.getMin()
test.push(3)
print test.getMin()
test.push(0)
print test.getMin()
test.push(5)
test.push(6)
print test.s
test.pop()
print test.s
print test.top()
print test.getMin()