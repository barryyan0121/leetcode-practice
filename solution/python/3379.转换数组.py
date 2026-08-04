class Solution:
    def constructTransformedArray(self, nums: list[int]) -> list[int]:
        size = len(nums)
        return [nums[(index + value) % size] for index, value in enumerate(nums)]


if __name__ == "__main__":
    test_cases = [
        (([3, -2, 1, 1],), [1, 1, 1, 3]),
        (([-1, 4, -1],), [-1, -1, 4]),
    ]
    for _, ((nums,), expected) in enumerate(test_cases):
        assert Solution().constructTransformedArray(nums) == expected
