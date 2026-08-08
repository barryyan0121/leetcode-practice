from typing import List


class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        dp = [1.0] + [0.0] * target
        for chance in prob:
            for heads in range(target, -1, -1):
                dp[heads] = dp[heads] * (1 - chance) + (
                    dp[heads - 1] * chance if heads else 0
                )
        return dp[target]


if __name__ == "__main__":
    test_cases = [([0.4], 1, 0.4), ([0.5, 0.5], 1, 0.5)]
    for _, (prob, target, expected) in enumerate(test_cases):
        assert abs(Solution().probabilityOfHeads(prob, target) - expected) < 1e-9
