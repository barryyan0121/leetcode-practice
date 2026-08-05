"""2449. 使数组相似的最少操作次数"""


class Solution:
    def makeSimilar(self, nums: list[int], target: list[int]) -> int:
        nums = [
            sorted(value for value in nums if value % 2 == parity) for parity in (0, 1)
        ]
        target = [
            sorted(value for value in target if value % 2 == parity)
            for parity in (0, 1)
        ]
        difference = sum(
            target_value - value
            for values, targets in zip(nums, target)
            for value, target_value in zip(values, targets)
            if target_value > value
        )
        return difference // 2


if __name__ == "__main__":
    test_cases = [(([8, 12, 6], [2, 14, 10]), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().makeSimilar(*args) == expected
