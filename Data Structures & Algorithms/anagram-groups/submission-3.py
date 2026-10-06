class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        strmap = defaultdict(list) # freq : str
        for s in strs:
            freq = [0] * 26 # 26 letters a - z, number is count
            for c in s:
                freq[ord('a') - ord(c)] += 1
            strmap[tuple(freq)].append(s)
        return list(strmap.values())
