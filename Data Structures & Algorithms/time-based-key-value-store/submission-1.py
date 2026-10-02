class TimeMap:

    def __init__(self):
        self.timemap = {} # key: list of [key, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = []
        self.timemap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        arrays = self.timemap.get(key, [])
        l, r = 0, len(arrays) - 1
        while l <= r:
            m = (l + r) // 2
            if arrays[m][1] <= timestamp:
                res = arrays[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
