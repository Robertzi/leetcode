class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [1,1]
        if n == 0 or n == 1:
            return 1
        else :
            l = len(result)
            for j in range(n-2):
                for i in range(l):
                    result[l] += resutl[l-1-i] +result[i]
                
                return result

x=Solution()
print(x.numTrees(19))
