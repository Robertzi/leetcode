class Solution:
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        arr = []
        ll = len(logs)
        res = [0 for i in range(n)]
        run = None
        for i in range(ll):
            arr.append() = logs[i].split(':')
            if(arr[i][1] == 'start'):
                run = arr[i][0]
            elif:

            

logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
x = Solution()
print(x.exclusiveTime(2,logs))