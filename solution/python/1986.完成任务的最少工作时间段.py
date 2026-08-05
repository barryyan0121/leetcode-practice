"""1986. 完成任务的最少工作时间段"""


class Solution:
    def minSessions(self, tasks: list[int], sessionTime: int) -> int:
        n = len(tasks)
        total = 1 << n
        valid = [False] * total
        valid[0] = True
        sums = [0] * total
        for mask in range(1, total):
            bit = mask & -mask
            index = bit.bit_length() - 1
            sums[mask] = sums[mask ^ bit] + tasks[index]
            valid[mask] = sums[mask] <= sessionTime
        dp = [n + 1] * total
        dp[0] = 0
        for mask in range(1, total):
            subset = mask
            while subset:
                if valid[subset]:
                    dp[mask] = min(dp[mask], dp[mask ^ subset] + 1)
                subset = (subset - 1) & mask
        return dp[-1]


if __name__ == "__main__":
    test_cases = [(([1, 2, 3], 3), 2), (([3, 1, 3, 1, 1], 8), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minSessions(*args) == expected
