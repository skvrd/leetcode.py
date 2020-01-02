# 244. Shortest Word Distance II

[Original Problem](https://leetcode.com/problems/shortest-word-distance-ii/)

Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list. Your method will be called repeatedly many times with different parameters. 

### Example:
Assume that words = `["practice", "makes", "perfect", "coding", "makes"]`.

```
Input: word1 = “coding”, word2 = “practice”
Output: 3
```

```
Input: word1 = "makes", word2 = "coding"
Output: 1
```

### Note:
You may assume that *word1* **does not equal to** *word2*, and *word1* and *word2* are both in the list.

## Thoughts

Let's create a hashtable to store all positions of all words. I will require O(N) complexity
When we want to compare to words we will just brute force all possible distances between words, and select min. (This part probably can be optimized)
