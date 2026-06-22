class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        nums_1 = []
        i = 0

        while i < len(nums):
            if nums[i] == val:
                nums_1.append(nums[i])
                nums.pop(i)
            else:
                i += 1

        k = len(nums)
        return k