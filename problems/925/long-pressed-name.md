# 925. Long Pressed Name

[Original Problem](https://leetcode.com/problems/long-pressed-name/)

Your friend is typing his `name` into a keyboard.  Sometimes, when typing a character `c`, the key might get long pressed, and the character will be typed 1 or more times.

You examine the `typed` characters of the keyboard.  Return `True` if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

### Example 1:
```
Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
```
### Example 2:
```
Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
```
### Example 3:
```
Input: name = "leelee", typed = "lleeelee"
Output: true
```
### Example 4:
```
Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.
```

### Note:

1. name.length <= 1000
2. typed.length <= 1000
3. The characters of name and typed are lowercase letters.

## Thoughts

Very easy problem to solve with 2 pointers.
One pointer points to current symbol on `name` other pointer points to current char on `typed`.
Also we need to store last seen char in name, every new char in typed either should be char we already saw (last seen) or a next char from name.

Space complexity O(1), since we only store 2 pointers and 1 last_seen var
Execution Complexety O(M) where M is `max` of lens of `name` and `typed`. 