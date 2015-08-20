class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.real_capacity = 0
        self.timestamp = 0
        self.LC1 = {}
        self.LC2 = {}

    # @return an integer
    def get(self, key):
        if self.real_capacity == 0:
        	self.timestamp = 0
        	return -1
        if self.LC1.has_key(key):
        	self.LC2[key] = self.timestamp
        	self.timestamp += 1
        	return self.LC1[key]
        else:
        	return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
    	if self.real_capacity == 0:
    		self.timestamp = 0
        if self.real_capacity >= self.capacity:
        	if self.LC1.has_key(key) == False:
	        	least_used = min(self.LC2.values())
	        	for k,v in self.LC2.items():
	        		if v == least_used:
	        			least_used_key = k
	        			break
	        	del self.LC1[least_used_key]
	        	del self.LC2[least_used_key]
        else:
        	if self.LC1.has_key(key) == False:
        		self.real_capacity += 1
        self.timestamp += 1
        self.LC1[key]=value
        self.LC2[key]=self.timestamp


expect_res=[-1,19,17,-1,-1,-1,5,-1,12,3,5,5,1,-1,30,5,30,-1,-1,24,18,-1,18,-1,18,-1,4,29,30,12,-1,29,17,22,18,-1,20,-1,18,18,20]

test = LRUCache(10)
test.set(10,13)
test.set(3,17)
test.set(6,11)
test.set(10,5)
test.set(9,10)
print test.get(13) #-1 [9,10,6,3]
test.set(2,19)
print test.get(2) #19 [2,9,10,6,3]
print test.get(3) #17 [3,2,9,10,6]
test.set(5,25)
print test.get(8) #-1
test.set(9,22)
test.set(5,5)
test.set(1,30)
print test.get(11) #-1 [1,5,9,3,2,10,6]
test.set(9,12)
print test.get(7) #-1
print test.get(5) #5
print test.get(8) #-1
print test.get(9) #12 [9,5,1,3,2,10,6]
test.set(4,30)
test.set(9,3)
print test.get(9) #3 [9,4,5,1,3,2,10,6]
print test.get(10) #5
print test.get(10) #5 [10,9,4,5,1,3,2,6]
test.set(6,14) 
test.set(3,1)
print test.get(3) #1 [3,6,10,9,4,5,1,2]
test.set(10,11)
print test.get(8) #-1
test.set(2,14) # [10,2,3,6,9,4,5,1]
print test.get(1)
print test.get(5)
print test.get(4)
test.set(11,4)
test.set(12,24)
test.set(5,18)
print test.get(13)
test.set(7,23)
print test.get(8)
print test.get(12)
test.set(3,27)
test.set(2,12)
print test.get(5)
test.set(2,9)
test.set(13,4)
test.set(8,18)
test.set(1,7)
print test.get(6)
test.set(9,29)
test.set(8,21)
print test.get(5)
test.set(6,30)
test.set(1,12)
print test.get(10)
test.set(4,15)
test.set(7,22)
test.set(11,26)
test.set(8,17)
test.set(9,29)
print test.get(5)
test.set(3,4)
test.set(11,30)
print test.get(12)
test.set(4,29)
print test.get(3)
print test.get(9)
print test.get(6)
test.set(3,4)
print test.get(1)
print test.get(10)
test.set(3,29)
test.set(10,28)
test.set(1,20)
test.set(11,13)
print test.get(3)
test.set(3,12)
test.set(3,8)
test.set(10,9)
test.set(3,26)
print test.get(8)
print test.get(7)
print test.get(5)
test.set(13,17)
test.set(2,27)
test.set(11,15)
print test.get(12)
test.set(9,19)
test.set(2,15)
test.set(3,16)
print test.get(1)
test.set(12,17)
test.set(9,1)
test.set(6,19)
print test.get(4)
print test.get(5)
print test.get(5)
test.set(8,1)
test.set(11,7)
test.set(5,2)
test.set(9,28)
print test.get(1)
test.set(2,2)
test.set(7,4)
test.set(4,22)
test.set(7,24)
test.set(9,26)
test.set(13,28)
test.set(11,26)