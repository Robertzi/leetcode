class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [1, 1]
        if n == 0 or n == 1:
            return 1
        else:
            for j in range(n-1):
                result.append(0)
                for i in range(j+2):
                    result[j+2] += result[j+1-i] * result[i]
            return result[j+2]