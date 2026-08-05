"""2040. 两个有序数组的第 K 小乘积"""

from bisect import bisect_left, bisect_right


class Solution:
    def kthSmallestProduct(self, nums1: list[int], nums2: list[int], k: int) -> int:
        def count_at_most(value: int) -> int:
            count = 0
            for number in nums1:
                if number > 0:
                    count += bisect_right(nums2, value // number)
                elif number < 0:
                    threshold = -((-value) // number)
                    count += len(nums2) - bisect_left(nums2, threshold)
                elif value >= 0:
                    count += len(nums2)
            return count

        low, high = -(10**10), 10**10
        while low < high:
            middle = (low + high) // 2
            if count_at_most(middle) >= k:
                high = middle
            else:
                low = middle + 1
        return low


if __name__ == "__main__":
    test_cases = [(([2, 5], [3, 4], 2), 8)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().kthSmallestProduct(*args) == expected
