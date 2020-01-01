# 120. Triangle

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

```
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
```
The minimum path sum from top to bottom is `11` (i.e., `2 + 3 + 5 + 1 = 11`).

## Note:

Bonus point if you are able to do this using only `O(n)` extra space, where n is the total number of rows in the triangle.


# Thoughts

First of all min path from bottom to top is the same problem as min path from top to bottom, so we can sole either of those.

It seems like a pretty straight forward Dynamic Programming problem.

We will start from last row:

```
path = list(triangle[-1])
```
to get to any item on last row, is exactly value of the item.

From last row we will make our way to the top, going through each row. to get to each point in any row is:
```
path[i] = triangle[height][i] + min(path[i], path[i+1])
```
min between two close items on the prevous row + value of current point.

At the end `path[0]` will me min path to bottom