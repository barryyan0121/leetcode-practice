"""1885. 统计数对"""

from bisect import bisect_right


class Solution:
    def countPairs(self, nums1: list[int], nums2: list[int]) -> int:
        differences = sorted(a - b for a, b in zip(nums1, nums2))
        answer = 0
        for index, value in enumerate(differences):
            answer += len(differences) - bisect_right(differences, -value, index + 1)
        return answer


if __name__ == "__main__":
    test_cases = [(([2, 1, 2, 1], [1, 2, 1, 2]), 2)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().countPairs(*args) == expected
