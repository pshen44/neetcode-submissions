class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, v in enumerate(temperatures):
            while stack and v > stack[-1][1]:
                ti, tv = stack.pop()
                res[ti] = i - ti
            stack.append([i, v])
        return res
            