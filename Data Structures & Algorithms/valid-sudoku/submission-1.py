class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        k = int(math.sqrt(n))

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(n):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue
                
                print(rows)
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in boxes[(i//k,j//k)]:
                    return False
                
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                boxes[(i//k,j//k)].add(board[i][j])

        return True