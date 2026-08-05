"""2448. 使数组相等的最小开销"""


class Solution:
    def minCost(self, nums: list[int], cost: list[int]) -> int:
        pairs = sorted(zip(nums, cost))
        total = sum(weight for _, weight in pairs)
        half = (total + 1) // 2
        running = 0
        target = pairs[0][0]
        for value, weight in pairs:
            running += weight
            if running >= half:
                target = value
                break
        return sum(abs(value - target) * weight for value, weight in pairs)


if __name__ == "__main__":
    test_cases = [(([1, 3, 5, 2], [2, 3, 1, 14]), 8)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minCost(*args) == expected
