class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [4,8,5,6] TARGET = 11
        # hash = { 4 : 0 } number : idx
        # if diff in hash
        #   return [idx1, idx2]
        # hash[nums[i]] = i
        num_map = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in num_map:
                return [num_map[diff], i]
            num_map[nums[i]] = i
        