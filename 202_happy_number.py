class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        result = []
        flag = get_sum(n,result)
        return flag
		
def get_sum(x,result):
	ems = []
	while True:
		ems.append(x%10)
		x = x/10
		if x >= 10:
			continue
		else:
			ems.append(x)
			break
	add_sum = 0
	for em in ems:
		add_sum += em*em
	print add_sum
	if add_sum == 1:
		return True
	if add_sum in result:
		return False
	else:
		result.append(add_sum)
		return get_sum(add_sum,result)