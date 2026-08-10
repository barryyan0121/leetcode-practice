"""2499. 让数组不相等的最小总代价"""

from collections import Counter


class Solution:
    def minimumTotalCost(self, nums1: list[int], nums2: list[int]) -> int:
        equal = [
            index
            for index, (first, second) in enumerate(zip(nums1, nums2))
            if first == second
        ]
        counts = Counter(nums1[index] for index in equal)
        majority, frequency = max(
            counts.items(), key=lambda item: item[1], default=(0, 0)
        )
        need = max(0, 2 * frequency - len(equal))
        extra = [
            index
            for index, (first, second) in enumerate(zip(nums1, nums2))
            if first != second and first != majority and second != majority
        ]
        if len(extra) < need:
            return -1
        return sum(equal) + sum(sorted(extra)[:need])
