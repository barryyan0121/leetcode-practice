"""3701. 计算交替和"""


class Solution:
    def alternatingSum(self, nums: list[int]) -> int:
        return sum(
            value if index % 2 == 0 else -value for index, value in enumerate(nums)
        )


if __name__ == "__main__":
    test_cases = [(([1, 3, 5, 7],), -4), (([100],), 100)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().alternatingSum(*args) == expected
