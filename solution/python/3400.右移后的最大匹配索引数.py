class Solution:
    def maximumMatchingIndices(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        return max(
            sum(nums1[(index - shift) % n] == value for index, value in enumerate(nums2))
            for shift in range(n)
        )


if __name__ == "__main__":
    assert Solution().maximumMatchingIndices([3, 1, 2, 3, 1, 2], [1, 2, 3, 1, 2, 3]) == 6
    assert Solution().maximumMatchingIndices([1, 4, 2, 5, 3, 1], [2, 3, 1, 2, 4, 6]) == 3
