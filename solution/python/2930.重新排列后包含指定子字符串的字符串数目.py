class Solution:
    def stringCount(self, n: int) -> int:
        mod = 10**9 + 7
        dp = [[[0] * 2 for _ in range(3)] for _ in range(2)]
        dp[0][0][0] = 1
        for _ in range(n):
            next_dp = [[[0] * 2 for _ in range(3)] for _ in range(2)]
            for has_l in range(2):
                for e_count in range(3):
                    for has_t in range(2):
                        count = dp[has_l][e_count][has_t]
                        next_dp[has_l][e_count][has_t] = (
                            next_dp[has_l][e_count][has_t] + count * 23
                        ) % mod
                        next_dp[1][e_count][has_t] = (
                            next_dp[1][e_count][has_t] + count
                        ) % mod
                        next_dp[has_l][min(2, e_count + 1)][has_t] = (
                            next_dp[has_l][min(2, e_count + 1)][has_t] + count
                        ) % mod
                        next_dp[has_l][e_count][1] = (
                            next_dp[has_l][e_count][1] + count
                        ) % mod
            dp = next_dp
        return dp[1][2][1]


assert Solution().stringCount(4) == 12
