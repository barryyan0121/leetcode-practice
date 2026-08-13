class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return min(nums1) % 2 == 1 or all(value % 2 == 0 for value in nums1)


if __name__ == "__main__":
    test_cases = [
        ([1, 4, 7], True),
        ([2, 3], False),
        ([4, 6], True),
    ]
    for _, (nums1, expected) in enumerate(test_cases):
        assert Solution().uniformArray(nums1) == expected
