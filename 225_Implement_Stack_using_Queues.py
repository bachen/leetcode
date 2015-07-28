class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.s = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.s.append(x)

    # @return nothing
    def pop(self):
        if self.s == []:
            pass
        else:
            self.s.pop()

    # @return an integer
    def top(self):
        if self.s == []:
            return None
        else:
            return self.s[-1]

    # @return an boolean
    def empty(self):
        if self.s == []:
            return True
        else:
            return False

