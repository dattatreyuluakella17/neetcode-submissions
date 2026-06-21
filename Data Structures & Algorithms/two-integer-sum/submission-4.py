class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable= {}
        a= 0
        output = []
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashtable:
                return [hashtable[complement], i]
            hashtable[nums[i]] = i
        
        return output