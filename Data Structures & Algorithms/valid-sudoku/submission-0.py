class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check all three conditions

        # 1. check row duplicates

        for row in range(len(board)):
            seen = []
            for value in range(len(board[row])):

                if board[row][value].isdigit():

                    if board[row][value] not in seen:
                        seen.append(board[row][value])
                    else:
                        return False
        
        # 2. check col duplicates

        for col in range(len(board[0])):
            seen = []
            for row in range(len(board)):

                if board[row][col].isdigit():

                    if board[row][col] not in seen:
                        seen.append(board[row][col])

                    else:
                        return False

        # 3. check sub-boxes duplicates

        for row in range(len(board)):

            if row % 3 == 0:
                box1 = []
                box2 = []
                box3 = []
            
            for col in range(len(board[row])):

                if board[row][col].isdigit():
                    
                    if col < 3:
                        
                        if board[row][col] not in box1:
                            box1.append(board[row][col])
                        
                        else:
                            return False

                    elif col < 6:

                        if board[row][col] not in box2:
                            box2.append(board[row][col])
                        
                        else:
                            return False
                    
                    else:
                        
                        if board[row][col] not in box3:
                            box3.append(board[row][col])

                        else:
                            return False

        return True
                
                    
                    
        


        