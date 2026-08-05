from collections import Counter


class Solution:
    def countBlackBlocks(
        self, m: int, n: int, coordinates: list[list[int]]
    ) -> list[int]:
        black = set(map(tuple, coordinates))
        counts = Counter()
        for r, c in black:
            for i, j in ((r - 1, c - 1), (r - 1, c), (r, c - 1), (r, c)):
                if 0 <= i < m - 1 and 0 <= j < n - 1:
                    counts[i, j] += 1
        ans = [0] * 5
        for value in counts.values():
            ans[value] += 1
        ans[0] = (m - 1) * (n - 1) - sum(ans[1:])
        return ans


if __name__ == "__main__":
    assert Solution().countBlackBlocks(3, 3, [[0, 0]]) == [3, 1, 0, 0, 0]
