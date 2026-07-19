class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        blocks=[]
        for i in range(0,9,3):
            for j in range(0,9,3):
                blocks.append([i,j])
        for a in blocks:
            s=[]
            if board[a[0]][a[1]].isdigit(): s.append(board[a[0]][a[1]])
            if board[a[0]][a[1]+1].isdigit(): s.append(board[a[0]][a[1]+1]) 
            if board[a[0]][a[1]+2].isdigit(): s.append(board[a[0]][a[1]+2]) 
            if board[a[0]+1][a[1]].isdigit(): s.append(board[a[0]+1][a[1]]) 
            if board[a[0]+2][a[1]].isdigit(): s.append(board[a[0]+2][a[1]]) 
            if board[a[0]+1][a[1]+1].isdigit(): s.append(board[a[0]+1][a[1]+1]) 
            if board[a[0]+2][a[1]+2].isdigit(): s.append(board[a[0]+2][a[1]+2]) 
            if board[a[0]+1][a[1]+2].isdigit(): s.append(board[a[0]+1][a[1]+2]) 
            if board[a[0]+2][a[1]+1].isdigit(): s.append(board[a[0]+2][a[1]+1])
            if(len(s)!=len(set(s))):
                return False  
        for i in range(0,9):
            row,col = [],[]
            for a in board[i]: 
                if a.isdigit():
                    row.append(a)
            for a in board:
                if a[i].isdigit():
                    col.append(a[i])
            if len(row) != len(set(row)):
                return False
            if len(col) != len(set(col)):
                return False
        return True
            
        
