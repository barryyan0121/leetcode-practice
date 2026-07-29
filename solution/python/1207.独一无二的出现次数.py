from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = Counter(arr).values()
        return len(set(counts)) == len(counts)


if __name__ == "__main__":
    test_cases = [([1, 2, 2, 1, 1, 3], True), ([1, 2], False)]
    for _, (arr, expected) in enumerate(test_cases):
        assert Solution().uniqueOccurrences(arr) == expected
