from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        m1 = m2 = 0  # running totals minimums
        for c in reversed(cost):
            m = min(m1, m2)  # hold current minimum
            m1, m2 = m + c, m1
        return min(m1, m2)
