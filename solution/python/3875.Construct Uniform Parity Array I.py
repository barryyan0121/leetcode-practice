class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return True


if __name__ == "__main__":
    test_cases = [
        ([2, 3], True),
        ([4, 6], True),
    ]
    for _, (nums1, expected) in enumerate(test_cases):
        assert Solution().uniformArray(nums1) == expected
