class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        d = {1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',10:'Ten',
        11:'Eleven',12:'Twelve',13:'Thirteen',14:'Fourteen',15:'Fifteen',16:'Sixteen',17:'Seventeen',18:'Eighteen',19:'Nineteen',20:'Twenty',
        30:'Thirty',40:'Forty',50:'Fifty',60:'Sixty',70:'Seventy',80:'Eighty',90:'Ninety'}
        tmp = []
        res = []
        count = 0
        if num == 0:
        	return 'Zero'	
        while (num/1000):
        	tmp.append(num%1000)
        	num=num/1000
        	count += 1
        if num > 0:
        	tmp.append(num)
        	count += 1
        print tmp
        for i in xrange(count-1,-1,-1):
        	if i == 3:
        		res.append(d[tmp[i]]+' Billion')
        	elif i == 2:
        		if tmp[i] == 0:
        			continue
        		elif 20 >= tmp[i]:
        			res.append(d[tmp[i]]+' Million')
        		elif tmp[i] >= 100:
        			res.append(d[tmp[i]/100]+' Hundred')
        			if (tmp[i]%100) == 0:
        				res.append('Million')
        			elif 20 >= (tmp[i]%100):
        				res.append(d[tmp[i]%100]+' Million')
        			else:
        				m1 = tmp[i] - (tmp[i]/100)*100
        				m2 = tmp[i] - (tmp[i]/100)*100 - (m1/10)*10
        				m1 = m1 - m2
        				if m2 != 0:
        					res.append(d[m1]+' '+d[m2]+' Million')
        				else:
        					res.append(d[m1]+' Million')
        		else:
        			m1 = (tmp[i]/10)*10
        			m2 = tmp[i] - m1
        			if m2 != 0:
        				res.append(d[m1]+' '+d[m2]+' Million')
        			else:
        				res.append(d[m1]+' Million')
        	elif i == 1:
        		if tmp[i] == 0:
        			continue
        		elif 20 >= tmp[i]:
        			res.append(d[tmp[i]]+' Thousand')
        		elif tmp[i] >= 100:
        			res.append(d[tmp[i]/100]+' Hundred')
        			if (tmp[i]%100) == 0:
        				res.append('Thousand')
        			elif 20 >= (tmp[i]%100):
        				res.append(d[tmp[i]%100]+' Thousand')
        			else:
        				m1 = tmp[i] - (tmp[i]/100)*100
        				m2 = tmp[i] - (tmp[i]/100)*100 - (m1/10)*10
        				m1 = m1 - m2
        				if m2 != 0:
        					res.append(d[m1]+' '+d[m2]+' Thousand')
        				else:
        					res.append(d[m1]+' Thousand')
        		else:
        			m1 = (tmp[i]/10)*10
        			m2 = tmp[i] - m1
        			if m2 != 0:
        				res.append(d[m1]+' '+d[m2]+' Thousand')
        			else:
        				res.append(d[m1]+' Thousand')
        	else:
        		if tmp[i] == 0:
        			continue
        		elif 20 >= tmp[i]:
        			res.append(d[tmp[i]])
        		elif tmp[i] >= 100:
        			res.append(d[tmp[i]/100]+' Hundred')
        			if (tmp[i]%100) == 0:
        				continue
        			elif 20 >= (tmp[i]%100):
        				res.append(d[tmp[i]%100])
        			else:
        				m1 = tmp[i] - (tmp[i]/100)*100
        				m2 = tmp[i] - (tmp[i]/100)*100 - (m1/10)*10
        				m1 = m1 - m2
        				if m2 != 0:
        					res.append(d[m1]+' '+d[m2])
        				else:
        					res.append(d[m1])
        		else:
        			m1 = (tmp[i]/10)*10
        			m2 = tmp[i] - m1
        			if m2 != 0:
        				res.append(d[m1]+' '+d[m2])
        			else:
        				res.append(d[m1])
        r = ' '.join(res)
        return r

test = Solution()
print test.numberToWords(1)