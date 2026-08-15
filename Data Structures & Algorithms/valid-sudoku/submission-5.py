class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for num in row:
                if num == ".":
                    continue
                elif num not in seen:
                    seen.add(num)
                else:
                    return False
        
        for i in range(len(board)):
            seen = set()
            for j in range(len(board[0])):
                if board[j][i] == ".":
                    continue
                elif board[j][i] not in seen:
                    seen.add(board[j][i])
                else:
                    return False    
        
        for square in range(len(board)):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    elif board[row][col] not in seen:
                        seen.add(board[row][col])
                    else:
                        return False

        return True
        
