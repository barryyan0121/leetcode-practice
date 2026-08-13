"""3852. 不同频率的最小数对"""

from collections import Counter


class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        counts = Counter(nums)
        values = sorted(counts)
        for i, x in enumerate(values):
            for y in values[i + 1 :]:
                if counts[x] != counts[y]:
                    return [x, y]
        return [-1, -1]


if __name__ == "__main__":
    test_cases = [(([1, 1, 2, 2, 3, 4],), [1, 3]), (([1, 5],), [-1, -1]), (([7],), [-1, -1])]
    for args, expected in test_cases:
        assert Solution().minDistinctFreqPair(*args) == expected
