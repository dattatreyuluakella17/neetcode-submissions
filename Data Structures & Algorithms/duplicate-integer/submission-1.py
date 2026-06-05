class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        p = len(nums)
        if p<=1:
            return False
        for i in range(p):
            if nums[i]==nums[i-1]:
                return True
        return False
