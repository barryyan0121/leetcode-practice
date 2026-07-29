from typing import List


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        modulo = 1_000_000_007
        dp = [[0] * (limit + 1) for limit in rollMax]
        for face in range(6):
            dp[face][1] = 1
        for _ in range(n - 1):
            next_dp = [[0] * (limit + 1) for limit in rollMax]
            for face, limit in enumerate(rollMax):
                for count in range(1, limit + 1):
                    ways = dp[face][count]
                    if not ways:
                        continue
                    if count < limit:
                        next_dp[face][count + 1] = (
                            next_dp[face][count + 1] + ways
                        ) % modulo
                    for next_face in range(6):
                        if next_face != face:
                            next_dp[next_face][1] = (
                                next_dp[next_face][1] + ways
                            ) % modulo
            dp = next_dp
        return sum(sum(counts) for counts in dp) % modulo


if __name__ == "__main__":
    test_cases = [(2, [1, 1, 2, 2, 2, 3], 34), (2, [1, 1, 1, 1, 1, 1], 30)]
    for _, (n, roll_max, expected) in enumerate(test_cases):
        assert Solution().dieSimulator(n, roll_max) == expected
