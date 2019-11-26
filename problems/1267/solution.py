from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        connected = 0
        n = [0] * len(grid)
        m = [0] * len(grid[0])
        for i in range(len(n)):
            for j in range(len(m)):
                if grid[i][j] == 1:
                    n[i] += 1
                    m[j] += 1
        for i in range(len(n)):
            for j in range(len(m)):
                if grid[i][j] == 1 and (n[i] > 1 or m[j] > 1):
                    connected += 1
        return connected