class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strmap = defaultdict(list) # freq : word
        for s in strs:
            freq = [0] * 26 # letter indx to freq
            for c in s:
                freq[ord('a') - ord(c)] += 1
            strmap[tuple(freq)].append(s)
        return list(strmap.values())
