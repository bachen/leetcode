class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        length1 = len(haystack)
        length2 = len(needle)
        if length2 > length1:
            return -1
        elif length2 == length1:
            if haystack == needle:
                return 0
            else:
                return -1
        elif length2 == 0:
            return 0
        mark_h = 0
        mark_n = 0
        res = 0
        for i in range(length1-length2+1):
            res = mark_h
            while mark_n < length2:
                if haystack[mark_h] == needle[mark_n]:
                    mark_h += 1
                    mark_n += 1
                    if mark_n == length2:
                        return res
                else:
                    mark_h = res + 1
                    mark_n = 0
                    break
        return -1
