class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # temperatures = [30,38,30,36,35,40,28]
        # result = [1, 0, 1, 0, 0, 0, 0]
        # stack = [ (38, 1), (36, 3)
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            pair = [t, i]
            while stack and stack[-1][0] < pair[0]:
                res[stack[-1][1]] = pair[1] - stack[-1][1]
                stack.pop()
            stack.append(pair)
        return res
