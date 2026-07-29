from collections import defaultdict
from typing import List


class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        frequencies = defaultdict(int)
        max_frequency = answer = 0
        for index, value in enumerate(nums, 1):
            previous = counts[value]
            if previous:
                frequencies[previous] -= 1
            counts[value] += 1
            current = counts[value]
            frequencies[current] += 1
            max_frequency = max(max_frequency, current)
            if (
                max_frequency == 1
                or (
                    frequencies[max_frequency] * max_frequency + 1 == index
                    and frequencies[1] == 1
                )
                or (
                    frequencies[max_frequency] == 1
                    and (max_frequency - 1) * frequencies[max_frequency - 1]
                    + max_frequency
                    == index
                )
            ):
                answer = index
        return answer


if __name__ == "__main__":
    test_cases = [
        ([2, 2, 1, 1, 5, 3, 3, 5], 7),
        ([1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5], 13),
    ]
    for _, (nums, expected) in enumerate(test_cases):
        assert Solution().maxEqualFreq(nums) == expected
