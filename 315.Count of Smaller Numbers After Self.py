class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums)
        counts = [0]*l
        self.arr = []
        for k in range(l):
            counts[l-k-1] = self.insert(nums[l-k-1])
        return counts
    def insert(self, n):
        l=0
        r=len(self.arr)-1
        if not self.arr or n<self.arr[0]:
            self.arr.insert(0, n)
            return 0
        elif n>self.arr[r]:
            self.arr.append(n)
            return r+1
        else:
            while(l<r):
                m=(l+r)//2
                if n>self.arr[m]:
                    l=m+1
                elif n<=self.arr[m]:
                    r=m
            self.arr.insert(r,n)
            return r