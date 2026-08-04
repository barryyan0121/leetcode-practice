"""3563. 移除相邻字符后字典序最小的字符串"""


class Solution:
    def lexicographicallySmallestString(self, s: str) -> str:
        gralvenoti = s
        n = len(s)
        removable = [[False] * (n + 1) for _ in range(n + 1)]
        for index in range(n + 1):
            removable[index][index] = True

        def consecutive(left, right):
            difference = abs(ord(s[left]) - ord(s[right]))
            return difference == 1 or difference == 25

        for length in range(2, n + 1, 2):
            for left in range(n - length + 1):
                right = left + length
                for middle in range(left + 1, right, 2):
                    if (
                        consecutive(left, middle)
                        and removable[left + 1][middle]
                        and removable[middle + 1][right]
                    ):
                        removable[left][right] = True
                        break

        best = [""] * (n + 1)
        for left in range(n - 1, -1, -1):
            result = s[left] + best[left + 1]
            for right in range(left + 1, n, 2):
                if (
                    consecutive(left, right)
                    and removable[left + 1][right]
                    and best[right + 1] < result
                ):
                    result = best[right + 1]
            best[left] = result
        return best[0]


if __name__ == "__main__":
    test_cases = [
        (("abc",), "a"),
        (("bcda",), ""),
        (("zdce",), "zdce"),
    ]
    for _, ((s,), expected) in enumerate(test_cases):
        assert Solution().lexicographicallySmallestString(s) == expected
