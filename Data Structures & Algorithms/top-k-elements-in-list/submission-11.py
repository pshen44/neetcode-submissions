class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        num_list = []
        for num, count in count.items():
            num_list.append([count, num])
        num_list.sort()
        final = []
        while len(final) < k:
            final.append(num_list.pop()[1])
        return final