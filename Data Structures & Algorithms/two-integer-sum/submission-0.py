class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nummap = {}
        for i, n in enumerate(nums):
            if target - n in nummap:
                return [nummap[target - n], i]
            nummap[n] = i