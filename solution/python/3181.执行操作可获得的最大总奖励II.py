class Solution:
    def maxTotalReward(self, rewardValues: list[int]) -> int:
        reachable = 1
        for reward in sorted(rewardValues):
            reachable |= (reachable & ((1 << reward) - 1)) << reward
        return reachable.bit_length() - 1


if __name__ == "__main__":
    test_cases = [([1, 1, 3, 3], 4), ([1, 6, 4, 3, 2], 11)]
    for _, (reward_values, expected) in enumerate(test_cases):
        assert Solution().maxTotalReward(reward_values) == expected
