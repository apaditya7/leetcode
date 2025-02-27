class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row
        for col in range(0,9):
            seen = []
            for row in range(0,9):
                val = board[col][row]
                if val == ".":
                    continue
                elif val in seen:
                    return False
                else:
                    seen.append(val)
        # check columns
        for row in range(0,9):
            seen = []
            for col in range(0,9):
                val = board[col][row]
                if val == ".":
                    continue
                elif val in seen:
                    return False
                else:
                    seen.append(val)
        # check squares
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True
