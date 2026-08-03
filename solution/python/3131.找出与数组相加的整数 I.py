class Solution:
    def addedInteger(self, nums1: list[int], nums2: list[int]) -> int:
        return min(nums2) - min(nums1)


if __name__ == "__main__":
    test_cases = [([2, 6, 4], [9, 7, 5], 3), ([10], [5], -5)]
    for _, (nums1, nums2, expected) in enumerate(test_cases):
        assert Solution().addedInteger(nums1, nums2) == expected
