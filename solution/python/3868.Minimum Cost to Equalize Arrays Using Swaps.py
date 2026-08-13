from collections import defaultdict


class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
        counts: dict[int, int] = defaultdict(int)
        for value in nums1:
            counts[value] += 1
        for value in nums2:
            counts[value] -= 1

        result = 0
        for diff in counts.values():
            if diff % 2:
                return -1
            if diff > 0:
                result += diff // 2
        return result


if __name__ == "__main__":
    test_cases = [
        (([10, 20], [20, 10]), 0),
        (([10, 10], [20, 20]), 1),
        (([10, 20], [30, 40]), -1),
    ]
    for _, ((nums1, nums2), expected) in enumerate(test_cases):
        assert Solution().minCost(nums1, nums2) == expected
