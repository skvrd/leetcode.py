from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        def helper(nums):
            prev_max = 0
            curr_max  = 0
            for i, v in enumerate(nums):
                temp = curr_max
                curr_max = max(prev_max + v, curr_max)
                prev_max = temp
            return curr_max
        

        max1 = helper(nums[:-1])
        max2 = helper(nums[1:])
        
        return max(max1, max2)