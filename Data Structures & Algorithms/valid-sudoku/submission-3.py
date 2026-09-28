class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def isValidSet(series :List[str]) -> bool:
                s: set[str] = set()
                for c in series:
                    if c != ".":
                        if c in s:
                            return False
                        else:
                            s.add(c)

                return True


        # do 3 passes
        # -h
        for p in board:
            if isValidSet(p) == False:
                print ("fail: h")
                return False
        #  - v
        for c in range(0, 9):
            if isValidSet([
                board[0][c], board[1][c], board[2][c],
                board[3][c], board[4][c], board[5][c],
                board[6][c], board[7][c], board[8][c]]) ==  False:
                    print ("fail: v")
                    return False

        #  - square
        for s in range(0, 9):
            r1 = (s // 3) * 3
            r2 = r1 + 1
            r3 = r2 + 1
          
            c1 = (s % 3) * 3
            c2 = c1 + 1
            c3 = c2 + 1

            print (f" s = {s}, r1 = {r1}, c1 = {c1}")

            print(f"{board[r1][c1]}, {board[r1][c2]}, {board[r1][c3]}")
            print(f"{board[r2][c1]}, {board[r2][c2]}, {board[r2][c3]}")
            print(f"{board[r3][c1]}, {board[r3][c2]}, {board[r3][c3]}")
            
            if isValidSet([
                    board[r1][c1], board[r1][c2], board[r1][c3],
                    board[r2][c1], board[r2][c2], board[r2][c3],
                    board[r3][c1], board[r3][c2], board[r3][c3]
                ]) ==  False: 
                
                return False   
        return True

