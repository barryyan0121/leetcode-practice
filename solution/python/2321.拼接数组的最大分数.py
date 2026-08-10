"""2321. 拼接数组的最大分数"""


class Solution:
    def maximumsSplicedArray(self, nums1: list[int], nums2: list[int]) -> int:
        def best_gain(base, other):
            best = current = 0
            for a, b in zip(base, other):
                current = max(0, current + b - a)
                best = max(best, current)
            return sum(base) + best

        return max(best_gain(nums1, nums2), best_gain(nums2, nums1))
