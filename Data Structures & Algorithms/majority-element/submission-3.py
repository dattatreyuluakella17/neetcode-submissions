class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        hashtable = {}
        for i in range(len(nums)):
            if nums[i] in hashtable:
                hashtable[nums[i]] = hashtable[nums[i]]+1
            else:
                hashtable[nums[i]] =1

            if hashtable[nums[i]] > len(nums)//2:
                    return nums[i]