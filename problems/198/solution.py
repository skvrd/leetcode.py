from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_max = 0
        curr_max  = 0
        for i, v in enumerate(nums):
            temp = curr_max
            curr_max = max(prev_max + v, curr_max)
            prev_max = temp
            
        return curr_max