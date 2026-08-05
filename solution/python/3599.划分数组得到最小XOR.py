"""3599. 划分数组得到最小 XOR"""


class Solution:
    def minXor(self, nums: list[int], k: int) -> int:
        quendravil = nums
        n = len(quendravil)
        prefix = [0]
        for value in quendravil:
            prefix.append(prefix[-1] ^ value)
        dp = [[1 << 60] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for parts in range(1, k + 1):
            for end in range(parts, n + 1):
                dp[end][parts] = min(
                    max(dp[start][parts - 1], prefix[end] ^ prefix[start])
                    for start in range(parts - 1, end)
                )
        return dp[n][k]


if __name__ == "__main__":
    test_cases = [
        (([1, 2, 3], 2), 1),
        (([2, 3, 3, 2], 3), 2),
        (([1, 1, 2, 3, 1], 2), 0),
    ]
    for _, ((nums, k), expected) in enumerate(test_cases):
        assert Solution().minXor(nums, k) == expected
