from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        travel_time = 0
        # Following is not quite python iterator, 
        # I wonder how to make it better
        for i in range(len(points)-1):
            distances = [abs(points[i][0] - points[i+1][0]), 
                         abs(points[i][1] - points[i+1][1])]
            travel_time += max(distances)
        return travel_time