class Solution:
    def specialPerm(self, nums: list[int]) -> int:
        mod = 10**9 + 7
        n = len(nums)
        dp = [[0] * n for _ in range(1 << n)]
        for i in range(n):
            dp[1 << i][i] = 1
        for mask in range(1 << n):
            for last in range(n):
                if not dp[mask][last]:
                    continue
                for nxt in range(n):
                    if not mask >> nxt & 1 and (
                        nums[last] % nums[nxt] == 0 or nums[nxt] % nums[last] == 0
                    ):
                        dp[mask | 1 << nxt][nxt] = (
                            dp[mask | 1 << nxt][nxt] + dp[mask][last]
                        ) % mod
        return sum(dp[-1]) % mod


if __name__ == "__main__":
    assert Solution().specialPerm([2, 3, 6]) == 2
