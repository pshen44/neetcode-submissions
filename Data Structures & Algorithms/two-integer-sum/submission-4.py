class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index_dict = {}

        for i, num in enumerate(nums):
            num_index_dict[num] = i

        for i, num in enumerate(nums):
            difference = target - num
            if difference in num_index_dict and num_index_dict[difference] != i:
                return [i, num_index_dict[difference]]

        