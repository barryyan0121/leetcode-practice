class Solution:
    def minElement(self, nums: list[int]) -> int:
        return min(sum(map(int, str(number))) for number in nums)


if __name__ == "__main__":
    test_cases = [
        (([10, 12, 13, 14],), 1),
        (([1, 2, 3, 4],), 1),
        (([999, 19, 199],), 10),
    ]
    for _, ((nums,), expected) in enumerate(test_cases):
        assert Solution().minElement(nums) == expected
