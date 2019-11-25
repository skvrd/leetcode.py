# 1126 Minimum Time Visiting All Points

On a plane there are n points with integer coordinates `points[i] = [xi, yi]`. Your task is to find the minimum time in seconds to visit all points.

You can move according to the next rules:

* In one second always you can either move vertically, horizontally by one unit or diagonally (it means to move one unit vertically and one unit horizontally in one second).
* You have to visit the points in the same order as they appear in the array.

## Thoughts

1. To travel from `[x1, y1]` to `[x2, y2]` you need to find longest diagonal path and then move top or bottom. This way path from one point to another should be shortest, thus should take least amount of time.
