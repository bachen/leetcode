class MinStack:
    # initialize your data structure here.
    def __init__(self):
        self.s = []
        self.d = {}
        self.min = None

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.s.append(x)
        if self.d.has_key(x):
            self.d[x] += 1
        else:
            self.d[x] = 1
        if (self.min == None) | (self.min > x):
            self.min = x
            
    # @return nothing
    def pop(self):
        tmp = self.s.pop()
        self.d[tmp] -= 1
        if self.d[tmp] == 0:
            del self.d[tmp]
            if tmp == self.min:
                if self.d == {}:
                    self.min = None
                else:
                    self.min = min(self.d)

    # @return an integer
    def top(self):
        if self.s == []:
            return None
        return self.s[-1]

    # @return an integer
    def getMin(self):
        if self.s == []:
            return None
        return self.min

test = MinStack()
test.push(1)
test.push(2)
test.push(3)
print test.s
test.pop()
print test.s
print test.top()
print test.getMin()