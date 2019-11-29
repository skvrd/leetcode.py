## 1138. Alphabet Board Path

[Original problem](https://leetcode.com/problems/alphabet-board-path/)

On an alphabet board, we start at position `(0, 0)`, corresponding to character `board[0][0]`.
`board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]`.

## Thoughts
1. We need helper function to calculate position of each letter.
2. For each new letter, we will calculate distance from current position to the position of the new letter. 
3. Vertical and horizontal distances will be calculated separately. For example horizontal distance will be `x[old] - x[new]`, so if distance is less than 0, we need to go right and if more than 0 we need to go left. For vertical distance we need to go bot and top respectively. If both distances are 0, than we don't need to go anywhere.
4. We always would want to go top first (if it is possible) because from `z` we only can move top. and we always want to go bottom last, since we only can get to `z` by moving bottom from `u`.
