class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate_dict = {}
        for num in nums:
            if num not in duplicate_dict:
                duplicate_dict[num] = 0
            else:
                duplicate_dict[num] += 1
            if duplicate_dict[num] >= 1:
                return True
        return False
            
