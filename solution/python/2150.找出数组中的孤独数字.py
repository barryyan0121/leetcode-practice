"""2150. 找出数组中的孤独数字"""

from collections import Counter


class Solution:
    def findLonely(self, nums: list[int]) -> list[int]:
        counts = Counter(nums)
        return [
            value
            for value in nums
            if counts[value] == 1
            and value - 1 not in counts
            and value + 1 not in counts
        ]


if __name__ == "__main__":
    test_cases = [(([10, 6, 5, 8],), [10, 8])]
    for _, (args, expected) in enumerate(test_cases):
        assert sorted(Solution().findLonely(*args)) == sorted(expected)
