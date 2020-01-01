class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        path = list(triangle[-1])
        height = len(triangle) - 1
        while height > 0:
            height -= 1
            length = len(triangle[height])
            for i in range(length):
                path[i] = triangle[height][i] + min(path[i], path[i+1])
        return path[0]
            