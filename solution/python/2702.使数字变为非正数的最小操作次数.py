"""2702. 使数字变为非正数的最小操作次数"""


class Solution:
    def minOperations(self, nums: list[int], x: int, y: int) -> int:
        left, right = 0, max(nums) // y + 1
        while left < right:
            operations = (left + right) // 2
            needed = 0
            for value in nums:
                remaining = value - operations * y
                if remaining > 0:
                    needed += (remaining + x - y - 1) // (x - y)
            if needed <= operations:
                right = operations
            else:
                left = operations + 1
        return left


if __name__ == "__main__":
    test_cases = [(([3, 4], 2, 1), 3)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().minOperations(*args) == expected
