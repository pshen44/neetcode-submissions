class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[r] < nums[mid]:
                #right portion
                l = mid + 1
            else:
                #left portion
                r = mid
        pivot = l

        def bs(left, right):
            while left <= right:
                middle = (left + right) // 2
                if target > nums[middle]:
                    left = middle + 1
                elif target < nums[middle]:
                    right = middle - 1
                else:
                    return middle
            return -1
        
        res = bs(0, pivot - 1)
        if res != -1:
            return res
        
        return bs(pivot, len(nums) - 1)

            