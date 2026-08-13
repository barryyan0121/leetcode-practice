class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        mod = 10**9 + 7
        dp = [0] * (k + 1)
        dp[0] = 1
        for sticks in range(1, n + 1):
            next_dp = [0] * (k + 1)
            for visible in range(1, min(sticks, k) + 1):
                next_dp[visible] = (dp[visible - 1] + dp[visible] * (sticks - 1)) % mod
            dp = next_dp
        return dp[k]


if __name__ == "__main__":
    solver = Solution()
    assert solver.rearrangeSticks(3, 2) == 3
    assert solver.rearrangeSticks(5, 5) == 1
