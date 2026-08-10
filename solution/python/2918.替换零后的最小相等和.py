"""2918. 替换零后的最小相等和"""


class Solution:
    def minSum(self, nums1: list[int], nums2: list[int]) -> int:
        sum1, sum2 = sum(nums1), sum(nums2)
        zeros1, zeros2 = nums1.count(0), nums2.count(0)
        low1, low2 = sum1 + zeros1, sum2 + zeros2
        if not zeros1 and not zeros2:
            return sum1 if sum1 == sum2 else -1
        if not zeros1 and sum1 < low2:
            return -1
        if not zeros2 and sum2 < low1:
            return -1
        return max(low1, low2)


if __name__ == "__main__":
    assert Solution().minSum([3, 2, 0, 1, 0], [6, 5, 0]) == 12
