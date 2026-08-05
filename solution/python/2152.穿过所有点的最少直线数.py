"""2152. 穿过所有点的最少直线数"""


class Solution:
    def minimumLines(self, points: list[list[int]]) -> int:
        n = len(points)
        lines = []
        for i in range(n):
            for j in range(i + 1, n):
                mask = 0
                x1, y1 = points[i]
                x2, y2 = points[j]
                for k, (x, y) in enumerate(points):
                    if (x2 - x1) * (y - y1) == (y2 - y1) * (x - x1):
                        mask |= 1 << k
                lines.append(mask)
        full = (1 << n) - 1
        dp = [n] * (1 << n)
        dp[0] = 0
        for mask in range(1 << n):
            if dp[mask] == n:
                continue
            first = next((index for index in range(n) if not mask >> index & 1), n)
            if first == n:
                continue
            for line in lines:
                if line >> first & 1:
                    dp[mask | line] = min(dp[mask | line], dp[mask] + 1)
        return dp[full]


if __name__ == "__main__":
    test_cases = [(([[1, 2], [3, 4], [5, 6]],), 1)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minimumLines(*args) == expected
