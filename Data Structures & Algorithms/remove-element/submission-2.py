class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        t = len(nums)
        print(t)
        while i < t:
            if nums[i] == val:
                t = t-1
                nums[i] = nums[t]
            else:
                i += 1

        return t