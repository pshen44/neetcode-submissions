class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        fmap = defaultdict(list) # freq : word LIST
        # k : [blah, blah blah]
        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord('a') - ord(c)] += 1
            fmap[tuple(freq)].append(s)
        return list(fmap.values())
        