class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        k = int(math.sqrt(n))

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(n):
            for j in range(n):
                val = board[i][j]

                if val == ".":
                    continue

                box = (i // k, j // k)

                if val in rows[i] or val in cols[j] or val in boxes[box]:
                    return False

                rows[i].add(val)
                cols[j].add(val)
                boxes[box].add(val)

        return True