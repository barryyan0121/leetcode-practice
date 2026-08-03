class Solution:
    def numberOfPairs(self, nums1: list[int], nums2: list[int], k: int) -> int:
        return sum(value % (other * k) == 0 for value in nums1 for other in nums2)


if __name__ == "__main__":
    test_cases = [([1, 3, 4], [1, 3], 1, 4), ([1, 2, 4], [2, 4], 1, 3)]
    for _, (nums1, nums2, k, expected) in enumerate(test_cases):
        assert Solution().numberOfPairs(nums1, nums2, k) == expected
