from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        x, y = click[0], click[1]
        steps = [
            (1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)
        ]
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        if board[x][y] == 'E':
            count = 0
            for step in steps:
                x1, y1 = x+step[0], y+step[1]
                if  not(0 <= x1 < len(board)):
                    continue
                if  not(0 <= y1 < len(board[0])):
                    continue
                if board[x1][y1] == 'M':
                    count += 1
            if count == 0:
                board[x][y] = 'B'
                for step in steps:
                    x1, y1 = x+step[0], y+step[1]
                    if  not(0 <= x1 < len(board)):
                        continue
                    if  not(0 <= y1 < len(board[0])):
                        continue
                    if board[x1][y1] == 'E':
                        
                        self.updateBoard(board, [x1,y1])
            else:
                board[x][y] = str(count) 
        return board
        