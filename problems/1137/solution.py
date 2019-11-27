class Solution:
    def tribonacci(self, n: int) -> int:
        cache = {}
        def helper(n: int) -> int:
            if cache.get(n, False):
                return cache[n]
            if n <= 0:
                return 0
            if n == 1:
                return 1
            if n == 2: 
                return 1
            T = helper(n-1) + helper(n-2) + helper(n-3)
            cache[n] = T
            return T
        return helper(n)