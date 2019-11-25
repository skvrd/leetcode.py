# 1267. Count Servers that Communicate

[Original problem](https://leetcode.com/problems/minimum-time-visiting-all-points/)

You are given a map of a server center, represented as a `m * n` integer matrix `grid`, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.

## Thoughts

### Iteration 1

1. Naive approach would be to iterate through entire grid and for each computer check it's row and column to see if it has other computers to communicate with.

### Iteration 2
1. We can create 2 lists one length of `n` and another with length of `m`, in those lists we will store how many servers located in each row and in each column.
2. We will iterate through `grid` and fill those arrays. 
3. Once we are done, we will iterate through the grid one more time, and for each computer we will check if numbers of computer in its column or row is more than 1, thus computer is connected to network.