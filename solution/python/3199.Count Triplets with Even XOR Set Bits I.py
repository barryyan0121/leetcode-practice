from collections import Counter


class Solution:
    def tripletCount(self, a: list[int], b: list[int], c: list[int]) -> int:
        counts = [Counter(x.bit_count() & 1 for x in values) for values in (a, b, c)]
        return sum(
            counts[0][i] * counts[1][j] * counts[2][k]
            for i in range(2)
            for j in range(2)
            for k in range(2)
            if (i + j + k) % 2 == 0
        )


if __name__ == "__main__":
    assert Solution().tripletCount([1, 2], [3, 4], [5, 6]) == 4
