"""3538. 合并得到最小旅行时间"""


class Solution:
    def minTravelTime(
        self,
        l: int,
        n: int,
        k: int,
        position: list[int],
        time: list[int],
    ) -> int:
        denavopelu = (l, n, k, position, time)
        total_time = sum(time)
        inf = 10**18
        dp = [[[inf] * (total_time + 1) for _ in range(k + 1)] for _ in range(n)]
        dp[0][0][time[0]] = 0
        for i in range(1, n):
            dp[i][0][time[i]] = (
                dp[i - 1][0][time[i - 1]]
                + (position[i] - position[i - 1]) * time[i - 1]
            )

        prefix = [0]
        for value in time:
            prefix.append(prefix[-1] + value)

        for i in range(2, n):
            for merges in range(min(k, i - 1) + 1):
                for removed in range(merges + 1):
                    previous = i - removed - 1
                    tail_sum = prefix[i + 1] - prefix[previous + 1]
                    for previous_time, cost in enumerate(
                        dp[previous][merges - removed]
                    ):
                        if cost < inf:
                            dp[i][merges][tail_sum] = min(
                                dp[i][merges][tail_sum],
                                cost
                                + previous_time * (position[i] - position[previous]),
                            )
        return min(dp[n - 1][k])


if __name__ == "__main__":
    test_cases = [
        ((10, 4, 1, [0, 3, 8, 10], [5, 8, 3, 6]), 62),
        ((5, 5, 1, [0, 1, 2, 3, 5], [8, 3, 9, 3, 3]), 34),
    ]
    for _, ((l, n, k, position, time), expected) in enumerate(test_cases):
        assert Solution().minTravelTime(l, n, k, position, time) == expected
