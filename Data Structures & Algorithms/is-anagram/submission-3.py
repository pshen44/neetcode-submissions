class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cmap = {} # char : count

        for char in s:
            cmap[char] = 1 + cmap.get(char, 0)
        
        for char in t:
            cmap[char] = cmap.get(char, 0) - 1
        
        return all(count == 0 for count in cmap.values())