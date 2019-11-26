# 1268. Search Suggestions System

[Original problem](https://leetcode.com/problems/search-suggestions-system/)

Given an array of strings `products` and a string `searchWord`. We want to design a system that suggests at most three product names from `products` after each character of `searchWord` is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return list of lists of the suggested `products` after each character of `searchWord` is typed. 

### Example 1:

```
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
```


## Thoughts

### Iteration 1
1. It seems to me that the easiest solution would be to create a so-called [Trie](https://en.wikipedia.org/wiki/Trie)
2. First we will implement `Trie` class with following methods:
    * `insert(word)`
    * `get_suggesions(prefix, number=3)`
3. Iterate for every prefix of the given word and find 3 suggestions.

This looks too easy to be true... but it worked just fine.
