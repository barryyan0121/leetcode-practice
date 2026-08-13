class Solution:
    def findMaximumLength(self, nums: list[int]) -> int:
        prefix = [0]
        for value in nums:
            prefix.append(prefix[-1] + value)
        n = len(nums)
        thresholds = [0]
        states = [(0, 0)]
        dp = [0] * (n + 1)
        last_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            target = prefix[i]
            best_dp, best_start = (0, 0)
            for threshold, state in zip(thresholds, states):
                if threshold <= target and state > (best_dp, best_start):
                    best_dp, best_start = state
            dp[i] = best_dp + 1
            last_sum[i] = prefix[i] - best_start
            thresholds.append(prefix[i] + last_sum[i])
            states.append((dp[i], prefix[i]))
        return dp[n]


assert Solution().findMaximumLength([5, 2, 2]) == 1
assert Solution().findMaximumLength([1, 2, 3, 4]) == 4
