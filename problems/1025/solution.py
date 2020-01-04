class Solution:
    def divisorGame(self, N: int, cache=None) -> bool:
        if N <= 1:
            return False

        if not cache:
            cache = {1:False}
        
        if cache and cache.get(N, False): 
            return cache[N]
        
        for x in range(1,N):
            if N % x == 0 and not self.divisorGame(N-x, cache=cache):
                cache[N]=True
                return True
            
        return False