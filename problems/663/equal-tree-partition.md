# 663. Equal Tree Partition

[Original Problem](https://leetcode.com/problems/equal-tree-partition/)

Given a binary tree with `n` nodes, your task is to check if it's possible to partition the tree to two trees which have the equal sum of values after removing exactly one edge on the original tree.

### Example 1:
```
Input:     
    5
   / \
  10 10
    /  \
   2   3

Output: True
Explanation: 
    5
   / 
  10
      
Sum: 15

   10
  /  \
 2    3

Sum: 15
```
### Example 2:

```
Input:     
    1
   / \
  2  10
    /  \
   2   20

Output: False
Explanation: You can't split the tree into two trees with equal sum after removing exactly one edge on the tree.
```

### Note:

1. The range of tree node value is in the range of `[-100000, 100000]`.
2. `1 <= n <= 10000`


## Thoughts

We can do 2 recursions:
1. We will recurse to find sum of the underlying tree for each node,
2. We will recurse to find node which has underlying tree of exactly half of the sum of entire initial tree.