class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        i = 0
        while l > 0 and s[l-1] == ' ':
            l -= 1
        if(l == 0):
            return 0
        while l > 0 and s[l-1] !=' ':
            i += 1
            l -= 1
        return i