class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1n = len(s1)
        if len(s1) > len(s2):
            return False
        
        s1map = [0] * 26
        s2map = [0] * 26
        for c in s1:
            s1map[ord('a') - ord(c)] += 1

        l = 0
        for r in range(len(s2)):
            if s1map == s2map:
                return True
            s2map[ord('a') - ord(s2[r])] += 1
            if (r - l + 1) > s1n:
                s2map[ord('a') - ord(s2[l])] -= 1
                l += 1
        return False
            
         
