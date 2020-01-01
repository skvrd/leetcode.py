# 151. Reverse Words in a String

[Original Problem](https://leetcode.com/problems/reverse-words-in-a-string/)

Given an input string, reverse the string word by word.

### Example 1:

```
Input: "the sky is blue"
Output: "blue is sky the"
```
### Example 2:
```
Input: "  hello world!  "
Output: "world! hello"
```
Explanation: Your reversed string should not contain leading or trailing spaces.


### Example 3:

```
Input: "a good   example"
Output: "example good a"
```
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

### Notes
- A word is defined as a sequence of non-space characters.
- Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
- You need to reduce multiple spaces between two words to a single space in the reversed string.

## Thoughts

Seems like an easy task:
* Go through entire string and create stack of words we saw so far.
* pop words from stack and add them to the resulting string