class Solution:
    def maxNonDecreasingLength(self, nums1: list[int], nums2: list[int]) -> int:
        a = b = 1
        ans = 1
        for i in range(1, len(nums1)):
            na = 1 + max(
                a if nums1[i] >= nums1[i - 1] else 0,
                b if nums1[i] >= nums2[i - 1] else 0,
            )
            nb = 1 + max(
                a if nums2[i] >= nums1[i - 1] else 0,
                b if nums2[i] >= nums2[i - 1] else 0,
            )
            a, b = na, nb
            ans = max(ans, a, b)
        return ans


if __name__ == "__main__":
    assert Solution().maxNonDecreasingLength([2, 3, 1], [1, 2, 1]) == 2
