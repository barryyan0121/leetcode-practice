"""2969. 购买水果需要的最少金币数 II"""

from collections import deque


class Solution:
    def minimumCoins(self, prices: list[int]) -> int:
        buy = [0] * (len(prices) + 1)
        free = [0] * (len(prices) + 1)
        candidates = deque()
        for index in range(1, len(prices) + 1):
            buy[index] = min(buy[index - 1], free[index - 1]) + prices[index - 1]
            limit = (index + 1) // 2
            while candidates and candidates[0] < limit:
                candidates.popleft()
            free[index] = buy[index]
            if candidates:
                free[index] = min(free[index], buy[candidates[0]])
            while candidates and buy[candidates[-1]] >= buy[index]:
                candidates.pop()
            candidates.append(index)
        return free[-1]


if __name__ == "__main__":
    test_cases = [(([1, 10, 1, 1],), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minimumCoins(*args) == expected
