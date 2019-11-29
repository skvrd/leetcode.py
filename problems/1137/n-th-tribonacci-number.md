# 1137 N-th Tribonacci Number

[Original problem](https://leetcode.com/problems/n-th-tribonacci-number/)

The Tribonacci sequence Tn is defined as follows: 

T[0] = 0, T[1] = 1, T[2] = 1, and T[n+3] = T[n] + T[n+1] + T[n+2] for `n >= 0`.

Given `n`, return the value of Tn.

## Thoughts

### Iteration 1
1. There are couple of ways to solve this problem:
    * Recursion (with [memoization](https://en.wikipedia.org/wiki/Memoization)) without memoization we will have exponential algorithm,
    * or, Dynamic programming. Dynamic programming should consume less memory and be more time efficient, but I find recursion easier approach to follow, so I will stick with recursion for this problem.
    Both of which should be trivial.
