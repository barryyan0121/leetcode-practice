"""4007. 栅栏的最宽宽度"""

from collections import Counter


class Solution:
    def maximumWidth(self, planks: list[int]) -> int:
        frequency = Counter(planks)
        widths = Counter(frequency)
        heights = list(frequency)
        for height, amount in frequency.items():
            widths[2 * height] += amount // 2
        for left, first in enumerate(heights):
            for second in heights[left + 1 :]:
                widths[first + second] += min(frequency[first], frequency[second])
        return max(widths.values())


if __name__ == "__main__":
    test_cases = [(([1, 3, 2, 5, 7, 5, 4, 2, 1],), 4), (([2, 3, 7],), 1)]
    for _, (args, expected) in enumerate(test_cases):
        assert Solution().maximumWidth(*args) == expected
