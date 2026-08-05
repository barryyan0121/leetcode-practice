class Solution:
    def maxIncreasingCells(self, mat: list[list[int]]) -> int:
        cells = sorted(
            (v, i, j) for i, row in enumerate(mat) for j, v in enumerate(row)
        )
        rows = [0] * len(mat)
        cols = [0] * len(mat[0])
        p = 0
        while p < len(cells):
            q = p
            cur = []
            while q < len(cells) and cells[q][0] == cells[p][0]:
                _, i, j = cells[q]
                cur.append((i, j, max(rows[i], cols[j]) + 1))
                q += 1
            for i, j, d in cur:
                rows[i] = max(rows[i], d)
                cols[j] = max(cols[j], d)
            p = q
        return max(rows + cols)


if __name__ == "__main__":
    assert Solution().maxIncreasingCells([[3, 1], [3, 4]]) == 2
