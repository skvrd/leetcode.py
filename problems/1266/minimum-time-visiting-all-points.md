# 1126 Minimum Time Visiting All Points

[Original problem](https://leetcode.com/problems/minimum-time-visiting-all-points/)

On a plane there are n points with integer coordinates `points[i] = [xi, yi]`. Your task is to find the minimum time in seconds to visit all points.

You can move according to the next rules:

* In one second always you can either move vertically, horizontally by one unit or diagonally (it means to move one unit vertically and one unit horizontally in one second).
* You have to visit the points in the same order as they appear in the array.

## Thoughts

### Iteration 1
1. To travel from `[x1, y1]` to `[x2, y2]` you need to find longest diagonal path, then travel it, and then move top or bottom. This way path from one point to another should be shortest, thus should take least amount of time.
2. To find longest diagonal path we need:
    * Find horizontal and vertical distances from one point to another. For example to find horizontal distance `x` between two point `[x1, y1]` and `[x2, y2]` we need to do following: `x= abs(x1 - x2)`.
    * longest diagonal would be shortest distance among vertical and horizontal distances.
    * ....


### Iteration 2
1. Thinking trough `iteration 1` gave me following observation: we don't have to calculate maximum diagonal path, all we need to do is just find the maximum between vertical and horizontal distances, and this number will be the minimum travel time between 2 points.
