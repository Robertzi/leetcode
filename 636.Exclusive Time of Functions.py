class Solution:
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        stack = []
        res = [0] * n
        lasttime = 0
        for log in logs:
            target = log.split(':')
            target[0] = int(target[0])
            target[2] = int(target[2])
            if target[1] == 'start':
                if len(stack) > 0:
                    res[stack[-1]] += target[2] - lasttime - 1
                stack.append(target[0])
            else:
                top = stack.pop()
                res[top] += target[2] - lasttime + 1
            lasttime = target[2]
        return res


logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
x = Solution()
print(x.exclusiveTime(2, logs))
