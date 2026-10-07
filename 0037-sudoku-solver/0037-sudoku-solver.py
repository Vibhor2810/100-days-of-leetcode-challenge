class Solution(object):
    def solveSudoku(self, board):
        rows, cols, boxes = [0] * 9, [0] * 9, [0] * 9
        empty = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty.append((r, c))
                else:
                    bit = 1 << (int(board[r][c]) - 1)
                    rows[r] |= bit
                    cols[c] |= bit
                    boxes[r // 3 * 3 + c // 3] |= bit

        def solve(k):
            if k == len(empty):
                return True

            # Pick the most constrained remaining cell and move it to position k
            best, best_cnt = k, 10
            for idx in range(k, len(empty)):
                r, c = empty[idx]
                used = rows[r] | cols[c] | boxes[r // 3 * 3 + c // 3]
                cnt = 9 - bin(used).count('1')
                if cnt == 0:
                    return False        # dead end, backtrack immediately
                if cnt < best_cnt:
                    best, best_cnt = idx, cnt
            empty[k], empty[best] = empty[best], empty[k]

            r, c = empty[k]
            b = r // 3 * 3 + c // 3
            avail = ~(rows[r] | cols[c] | boxes[b]) & 0x1FF

            while avail:
                bit = avail & -avail    # lowest available digit
                avail ^= bit
                rows[r] |= bit; cols[c] |= bit; boxes[b] |= bit
                board[r][c] = str(bit.bit_length())

                if solve(k + 1):
                    return True

                rows[r] ^= bit; cols[c] ^= bit; boxes[b] ^= bit   # undo

            board[r][c] = '.'
            return False

        solve(0)