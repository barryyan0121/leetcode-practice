"""2040. 两个有序数组的第 K 小乘积"""

from bisect import bisect_left, bisect_right


class Solution:
    def kthSmallestProduct(self, nums1: list[int], nums2: list[int], k: int) -> int:
        def count(value: int) -> int:
            total = 0
            for number in nums1:
                if number > 0:
                    total += bisect_right(nums2, value // number)
                elif number < 0:
                    total += len(nums2) - bisect_left(nums2, -((-value) // number))
                else:
                    total += len(nums2) if value >= 0 else 0
            return total

        low, high = -(10**10), 10**10
        while low < high:
            middle = (low + high) // 2
            if count(middle) >= k:
                high = middle
            else:
                low = middle + 1
        return low


if __name__ == "__main__":
    test_cases = [(([2, 5], [3, 4], 2), 8), (([-4, -2, 0, 3], [2, 4], 6), 0)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().kthSmallestProduct(*args) == expected
