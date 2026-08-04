class Solution:
    def countPartitions(self, nums: list[int]) -> int:
        return len(nums) - 1 if sum(nums) % 2 == 0 else 0


if __name__ == "__main__":
    test_cases = [
        (([10, 10, 3, 7, 6],), 4),
        (([1, 2, 2],), 0),
        (([2, 4, 6, 8],), 3),
    ]
    for _, ((nums,), expected) in enumerate(test_cases):
        assert Solution().countPartitions(nums) == expected
