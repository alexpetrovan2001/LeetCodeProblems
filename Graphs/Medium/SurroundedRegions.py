from typing import List

class Solution:
    # Beats 58% time and 84% memory with not_flipped as set -> 84% time and 96% memory with not_flipped as dict
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return []

        not_flipped = dict()

        m = len(board)
        n = len(board[0])

        def dfs(row, col):
            not_flipped[(row, col)] = True

            if row-1 > 0 and board[row-1][col] == 'O' and (row-1, col) not in not_flipped:
                dfs(row-1, col)
            if row+1 < m-1 and board[row+1][col] == 'O' and (row+1, col) not in not_flipped:
                dfs(row+1, col)
            if col-1 > 0 and board[row][col-1] == 'O' and (row, col-1) not in not_flipped:
                dfs(row, col-1)
            if col+1 < n-1 and board[row][col+1] == 'O' and (row, col+1) not in not_flipped:
                dfs(row, col+1)

        for col in range(n):
            if board[0][col] == 'O':
                dfs(0, col)
            if board[m-1][col] == 'O':
                dfs(m-1, col)

        for row in range(m):
            if board[row][0] == 'O':
                dfs(row, 0)
            if board[row][n-1] == 'O':
                dfs(row, n-1)

        for row in range(m):
            for col in range(n):
                if board[row][col] == 'O' and (row, col) not in not_flipped:
                    board[row][col] = 'X'

    def solve2(self, board: List[List[str]]) -> None:
        # Beats 80% time and 29% memory with set -> 94% time and 29% memory with dict
        if not board:
            return []

        not_flipped = dict()

        m = len(board)
        n = len(board[0])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(row, col):
            not_flipped[(row, col)] = True

            for r, c in directions:
                new_row = row + r
                new_col = col + c
                if m > new_row >= 0 and n > new_col >= 0 and board[new_row][new_col] == 'O' and (
                new_row, new_col) not in not_flipped:
                    dfs(new_row, new_col)

        for col in range(n):
            if board[0][col] == 'O':
                dfs(0, col)
            if board[m - 1][col] == 'O':
                dfs(m - 1, col)

        for row in range(m):
            if board[row][0] == 'O':
                dfs(row, 0)
            if board[row][n - 1] == 'O':
                dfs(row, n - 1)

        for row in range(m):
            for col in range(n):
                if board[row][col] == 'O' and (row, col) not in not_flipped:
                    board[row][col] = 'X'


sol = Solution()
sol.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])