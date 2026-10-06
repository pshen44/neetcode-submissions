class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #brute
        intervals.sort(key = lambda x: x[0])
        res = []
        for i in range(len(intervals)):
            curr = intervals[i]
            if not res or res[-1][1] < curr[0]:
                    #no overlap
                res.append(curr)
            else:
                res[-1][1] = max(res[-1][1], curr[1])
        return res
        # intervals = [[1,3],[1,5],[6,7]]
        # res = [[1,3], 
