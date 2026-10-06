class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        if not s:
            return res
        numset = set()
        
        for r in range(len(s)):
            while s[r] in numset:
                numset.remove(s[l])
                l += 1
            else:
                numset.add(s[r])
            res = max(res, r - l + 1)
        return res
        # zxyz
        # set = {, x, y, z}
        # res = 3
