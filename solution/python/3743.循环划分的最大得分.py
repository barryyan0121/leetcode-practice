"""3743. 循环划分的最大得分"""


class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        tornequal = nums
        negative = -(1 << 60)
        picks_limit = min(2 * k, len(tornequal))
        answer = negative
        for initial in range(3):
            dp = [[negative] * 3 for _ in range(picks_limit + 1)]
            dp[0][initial] = 0
            for value in tornequal:
                for picks in range(picks_limit - 1, -1, -1):
                    for balance in range(3):
                        score = dp[picks][balance]
                        if score == negative:
                            continue
                        if balance < 2:
                            dp[picks + 1][balance + 1] = max(
                                dp[picks + 1][balance + 1], score + value
                            )
                        if balance:
                            dp[picks + 1][balance - 1] = max(
                                dp[picks + 1][balance - 1], score - value
                            )
            answer = max(
                answer, max(dp[picks][initial] for picks in range(picks_limit + 1))
            )
        return answer


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 3, 3], 2), 3),
        (([1, 2, 3, 3], 1), 2),
        (([1, 2, 3, 3], 4), 3),
    ]
    for _, ((nums, k), expected) in enumerate(test_cases):
        assert Solution().maximumScore(nums, k) == expected
