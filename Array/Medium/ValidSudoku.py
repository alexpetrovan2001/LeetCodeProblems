from typing import List


class Solution:
    # First sol to implement -> 20% time 80% memory
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            if not self.isValid(i):
                return False

        squares = []
        rows = []

        for i in range(9):
            rows.append([])
            for j in range(9):
                if board[j][i] != ".":
                    rows[i].append(board[j][i])

        for i in rows:
            if not self.isValid(i):
                return False

        square = 0
        for i in range(3):  # row
            for j in range(3):  # column
                squares.append([])
                for k in range(3):  # value to add to row
                    for l in range(3): # value to add to col
                        value = board[i * 3 + k][j * 3 + l]
                        if value != ".":
                            squares[square].append(value)
                square += 1

        for i in squares:
            if not self.isValid(i):
                return False

        return True

    @staticmethod
    def isValid(numbers: List[str]) -> bool:
        freq = dict()
        for i in numbers:
            if i != "." and i not in freq:
                freq[i] = 1
            elif i != ".":
                return False
        return True


    def isValidSudoku2(self, board: List[List[str]]) -> bool:
        # Balance between time and memory: 33% time 42% mem. If we use dicts instead of arrays, time lowers but memory increases
        rows = []
        cols = []
        squares = []

        for i in range(9):
            rows.append([])
            cols.append([])
            squares.append([])

        for i in range(9):
            for j in range(9):
                value = board[i][j]
                if value != ".":
                    if value not in rows[i]:
                        rows[i].append(value)
                    else:
                        return False
                    if value not in cols[j]:
                        cols[j].append(value)
                    else:
                        return False
                    rowMultiplier = i//3
                    colMultiplier = j//3
                    if value not in squares[rowMultiplier*3 + colMultiplier]:
                        squares[rowMultiplier*3 + colMultiplier].append(value)
                    else:
                        return False
        return True

sol = Solution()
sol.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])
